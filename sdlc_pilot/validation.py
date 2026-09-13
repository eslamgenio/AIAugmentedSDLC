"""Schema and handoff validation; business correctness requires an evaluator."""

from importlib.resources import files
from datetime import datetime, timezone
import json
import re
from jsonschema import Draft202012Validator, FormatChecker
from .store import StoreError


class ValidationFailure(ValueError):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


def require(condition, code, message):
    if not condition:
        raise ValidationFailure(code, message)


def same(a, b):
    return json.dumps(a, sort_keys=True, allow_nan=False) == json.dumps(b, sort_keys=True, allow_nan=False)


def index(items, field):
    result = {item[field]: item for item in items}
    require(len(result) == len(items), "duplicate_id", f"Duplicate {field}")
    return result


def pointer(document, location):
    require(location.startswith("/"), "evidence", "Evidence must use an absolute JSON pointer")
    try:
        for segment in location[1:].split("/"):
            require(re.search(r"~(?![01])",segment) is None, "evidence", "Invalid pointer escape")
            key = segment.replace("~1", "/").replace("~0", "~")
            if isinstance(document, list):
                require(key.isdecimal() and str(int(key)) == key, "evidence", "Invalid array index")
                document = document[int(key)]
            else:
                document = document[key]
        return document
    except (KeyError, IndexError, TypeError, ValueError) as exc:
        raise ValidationFailure("evidence", "Evidence location does not resolve") from exc


SOURCE_FIELDS = {
    "A05": ("requirements", "baseline_id", "baseline_version"),
    "A04": ("acceptance_criteria",), "E09": ("approval",),
    "A15": ("test_scope",), "A06": ("risks",), "A09": ("design_rules",),
    "E06": ("coverage_rules", "test_template_fields"), "E01": ("business_rules",),
}


def format_checker():
    checker = FormatChecker()

    @checker.checks("date-time", raises=(ValueError, TypeError))
    def timestamp(value):
        if not isinstance(value, str):
            return True
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:[0-5]\d(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})", value):
            return False
        return datetime.fromisoformat(value.upper().replace("Z", "+00:00")).tzinfo is not None

    return checker


class PilotValidator:
    def __init__(self, store, *, fixture_mode=False, trusted_approvals=None):
        self.store = store
        self.fixture_mode = fixture_mode
        # Populated by a trusted human-input adapter, never by model output.
        # Maps the approved E09 source digest to the verified decision object.
        self.trusted_approvals = trusted_approvals or {}
        self.schema = json.loads(files("sdlc_pilot").joinpath("contracts.schema.json").read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(self.schema)

    def structural(self, document, profile):
        try:
            json.dumps(document,allow_nan=False)
        except (ValueError,TypeError) as exc:
            raise ValidationFailure('schema','Payload contains non-JSON or non-finite values') from exc
        require(profile in ("pilotInput", "creationBundle", "reviewBundle", "runRecord"), "profile", "Unknown profile")
        validator = Draft202012Validator({"$ref": f"#/$defs/{profile}", "$defs": self.schema["$defs"]}, format_checker=format_checker())
        error = next(validator.iter_errors(document), None)
        if error:
            path = "/" + "/".join(str(x) for x in error.absolute_path)
            raise ValidationFailure("schema", f"{path}: {error.message}")
        require(self.fixture_mode == document["synthetic_fixture"], "fixture_boundary",
                "Synthetic examples require fixture mode; fixture mode cannot validate live artifacts")

    def _read(self, reference):
        try:
            return self.store.read(reference)
        except StoreError as exc:
            raise ValidationFailure("source_integrity", str(exc)) from exc

    def _scope(self, artifact, baseline):
        for field in ("project_id", "run_id", "iteration_id"):
            require(artifact[field] == baseline[field], "scope", f"Mismatched {field}")
        for field in ("baseline_id", "baseline_version"):
            require(artifact["payload"][field] == baseline[field], "stale_baseline", f"Mismatched {field}")

    def _sources(self, artifact, baseline):
        refs = artifact["source_artifact_versions"]
        by_id = index(refs, "artifact_id")
        require("PILOT-INPUT" in by_id, "source_set", "Missing pinned PILOT-INPUT")
        for reference in refs:
            require(reference["project_id"] == artifact["project_id"] and reference["iteration_id"] == artifact["iteration_id"],
                    "scope", "Source belongs to another project or iteration")
            self._read(reference)
        require(same(self._read(by_id["PILOT-INPUT"]), baseline), "stale_baseline", "Pinned input differs from supplied baseline")
        return by_id

    def validate_input(self, baseline):
        self.structural(baseline, "pilotInput")
        sources = index(baseline["sources"], "artifact_id")
        require(set(sources) == set(SOURCE_FIELDS), "source_set", "Input requires exactly the eight specified upstream sources")
        approval = baseline["approval"]
        require(approval["baseline_id"] == baseline["baseline_id"] and approval["baseline_version"] == baseline["baseline_version"],
                "approval_scope", "Approval covers a different baseline")
        require(datetime.fromisoformat(approval["timestamp"].replace("Z", "+00:00")) <= datetime.now(timezone.utc),
                "approval_time", "Approval is dated in the future")
        for id, fields in SOURCE_FIELDS.items():
            reference = sources[id]
            require(reference["project_id"] == baseline["project_id"] and reference["iteration_id"] == baseline["iteration_id"],
                    "scope", "Upstream source belongs to another project or iteration")
            if self.fixture_mode and reference["sha256"] == "0" * 64:
                continue
            source = self._read(reference)
            require(source.get("synthetic_fixture") == self.fixture_mode, "fixture_boundary", "Source fixture mode differs")
            payload = source.get("payload", {})
            require(all(k in payload and same(payload[k], baseline[k]) for k in fields),
                    "source_content", f"{id} does not substantiate its normalized input fields")
        if not self.fixture_mode:
            trusted = self.trusted_approvals.get(sources["E09"]["sha256"])
            require(trusted is not None and same(trusted, approval), "untrusted_approval",
                    "No independently supplied approval attestation matches the E09 digest")
        requirements = index(baseline["requirements"], "requirement_id")
        criteria = index(baseline["acceptance_criteria"], "criterion_id")
        require(all(c["requirement_id"] in requirements for c in criteria.values()), "unknown_id", "Unknown requirement in criteria")
        require({c["requirement_id"] for c in criteria.values()} == set(requirements), "coverage", "A requirement has no acceptance criteria")
        index(baseline["risks"], "risk_id")
        require(all(set(r["criterion_ids"]) <= set(criteria) for r in baseline["risks"]), "unknown_id", "Risk references unknown criterion")
        required_fields = set(self.schema["$defs"]["testCase"]["required"])
        require(set(baseline["test_template_fields"]) == required_fields, "template", "Test template differs from the pilot test-case profile")

    def validate_creation(self, candidate, baseline, *, previous_review=None, previous_candidate=None):
        self.validate_input(baseline)
        self.structural(candidate, "creationBundle")
        self._scope(candidate, baseline)
        sources = self._sources(candidate, baseline)
        payload = candidate["payload"]
        criteria = index(baseline["acceptance_criteria"], "criterion_id")
        req_ids = {r["requirement_id"] for r in baseline["requirements"]}
        tests = index(payload["test_cases"]["payload"]["cases"], "test_id")
        for test in tests.values():
            require(set(test["criterion_ids"]) <= set(criteria) and set(test["requirement_ids"]) <= req_ids,
                    "unknown_id", "Test references unknown requirements or criteria")
            require({criteria[c]["requirement_id"] for c in test["criterion_ids"]} == set(test["requirement_ids"]),
                    "traceability", "Test requirement links disagree with its criteria")
        resources = index(payload["test_resources"]["payload"]["resources"], "test_id")
        require(set(resources) == set(tests), "resources", "Resource records must match the test IDs exactly")
        for id, resource in resources.items():
            require(all(same(resource[k], tests[id][k]) for k in ("preconditions", "data", "expected")),
                    "resources", f"Resource view differs from test {id}")
        questions = payload["coverage_questions"]["payload"]
        index(questions["questions"], "question_id")
        for question in questions["questions"]:
            require(question["status"] != "RESOLVED" or bool(question["resolution"] and question["resolution"].strip()),
                    "question", "Resolved question lacks its resolution")
        require(set(questions["automation_candidate_test_ids"]) <= set(tests), "unknown_id", "Unknown automation candidate")
        for key in ("test_cases", "test_resources", "coverage_questions"):
            require(payload[key]["artifact_version"] == candidate["artifact_version"], "child_version", "Child version differs from parent")
        actions = index(payload["revision_actions"], "finding_id")
        if previous_review is None:
            require(not actions and "A17" not in sources, "revision_context", "Revision requires the previous review")
        else:
            require(previous_candidate is not None and "A17" in sources and "A16" in sources,
                    "revision_context", "Revision needs pinned previous candidate and review")
            require(same(self._read(sources["A17"]), previous_review) and same(self._read(sources["A16"]), previous_candidate),
                    "revision_context", "Previous artifacts do not match pinned sources")
            self.structural(previous_review, "reviewBundle")
            self.structural(previous_candidate, "creationBundle")
            self._scope(previous_review, baseline)
            self._scope(previous_candidate, baseline)
            require(previous_review["payload"]["candidate"] == sources["A16"], "stale_review", "Previous review covers another candidate")
            findings = index(previous_review["payload"]["review"]["payload"]["findings"], "finding_id")
            require(set(actions) == set(findings), "revision_actions", "Every prior finding needs one revision action")
            require(all(set(a["affected_test_ids"]) <= set(tests) for a in actions.values()), "unknown_id", "Revision action references unknown tests")
            require(tuple(map(int, candidate["artifact_version"].split('.'))) > tuple(map(int, previous_candidate["artifact_version"].split('.'))),
                    "version", "Revision must increment artifact version")
            old_tests = previous_candidate["payload"]["test_cases"]["payload"]["cases"]
            for old in old_tests:
                for new in tests.values():
                    if same(old["data"], new["data"]) and same(old["steps"], new["steps"]):
                        require(old["test_id"] == new["test_id"], "test_identity", "Unchanged test was renumbered")
        return tests

    def validate_review(self, review, candidate, baseline, candidate_reference, *, previous_review=None, previous_candidate=None):
        tests = self.validate_creation(candidate, baseline, previous_review=previous_review, previous_candidate=previous_candidate)
        self.structural(review, "reviewBundle")
        self._scope(review, baseline)
        refs = self._sources(review, baseline)
        payload = review["payload"]
        require(same(payload["candidate"], candidate_reference) and refs.get("A16") == candidate_reference,
                "stale_review", "Review does not reference the selected current candidate")
        require(same(self._read(candidate_reference), candidate), "stale_review", "Candidate bytes differ from selected reference")
        criteria = index(baseline["acceptance_criteria"], "criterion_id")
        coverage = index(payload["traceability"]["payload"]["coverage"], "criterion_id")
        require(set(coverage) == set(criteria), "coverage", "Review must account for every criterion exactly once")
        for id, row in coverage.items():
            require(row["requirement_id"] == criteria[id]["requirement_id"], "traceability", "Matrix requirement differs")
            require(set(row["test_ids"]) <= set(tests), "unknown_id", "Matrix references an unknown test")
            require(all(id in tests[t]["criterion_ids"] for t in row["test_ids"]), "traceability", "Matrix link not present in test")
            require(bool(row["test_ids"]) == (row["status"] == "COVERED"), "coverage", "Coverage status disagrees with test links")
        gaps = payload["gaps"]["payload"]
        require(set(gaps["gap_criterion_ids"]) == {id for id,r in coverage.items() if r["status"] == "GAP"},
                "coverage", "Gap report disagrees with traceability matrix")
        for group in gaps["duplicate_groups"]:
            require(set(group["test_ids"]) <= set(tests), "unknown_id", "Duplicate group contains unknown test")
        detail = payload["review"]["payload"]
        findings = index(detail["findings"], "finding_id")
        for finding in findings.values():
            require(set(finding["test_ids"]) <= set(tests) and set(finding["criterion_ids"]) <= set(criteria), "unknown_id", "Finding references unknown IDs")
            evidence = finding["evidence"]
            target = candidate if evidence["artifact_id"] == "A16" else baseline
            version = candidate["artifact_version"] if target is candidate else baseline["baseline_version"]
            require(evidence["artifact_id"] in ("A16", "PILOT-INPUT") and evidence["artifact_version"] == version,
                    "evidence", "Evidence must reference current candidate or input")
            pointer(target, evidence["location"])
        checks = index(detail["previous_finding_checks"], "finding_id")
        prior = previous_review["payload"]["review"]["payload"]["findings"] if previous_review else []
        require(set(checks) == {f["finding_id"] for f in prior}, "revision_actions", "Reviewer must check every previous finding")
        for key in ("traceability", "gaps", "review"):
            require(payload[key]["artifact_version"] == review["artifact_version"], "child_version", "Child version differs from parent")
        if detail["recommendation"] == "READY":
            require(not gaps["gap_criterion_ids"] and not gaps["duplicate_groups"] and all(f["status"] == "RESOLVED" for f in findings.values()),
                    "not_ready", "READY has gaps, duplicates or unresolved findings")
            require(all(c["verified_resolved"] for c in checks.values()), "not_ready", "Previous finding remains unresolved")
            require(not any(q["blocking"] and q["status"] == "OPEN" for q in candidate["payload"]["coverage_questions"]["payload"]["questions"]),
                    "not_ready", "Blocking question remains open")
            signatures = [json.dumps([t["data"],t["steps"],t["expected"]],sort_keys=True) for t in tests.values()]
            require(len(signatures) == len(set(signatures)), "not_ready", "Exact duplicate tests remain")
        return detail["recommendation"]

    def validate_run(self, record, baseline, *, trusted_final_approval=None, previous_review=None, previous_candidate=None):
        self.structural(record, "runRecord")
        self.validate_input(baseline)
        require(all(record[k] == baseline[k] for k in ("project_id","run_id","iteration_id","baseline_id","baseline_version")), "scope", "Run scope differs from input")
        source_index = index(record["sources"], "artifact_id")
        require("PILOT-INPUT" in source_index and same(self._read(source_index["PILOT-INPUT"]), baseline), "stale_baseline", "Run input differs")
        for r in record["sources"]:
            self._read(r)
        index(record["events"], "sequence")
        require([e["sequence"] for e in record["events"]] == sorted(e["sequence"] for e in record["events"]), "events", "Event sequence is unordered")
        require(record["events"][-1]["to_state"] == record["state"], "events", "Last event does not match current state")
        for a,b in zip(record["events"],record["events"][1:]):
            require(a["to_state"] == b["from_state"], "events", "Event history is discontinuous")
        index(record["operations"], "operation_key")
        usage, limits = record["usage"], record["limits"]
        over = (usage["revisions"] > limits["max_revisions"] or usage["requests"] > limits["max_requests"] or
                usage["input_tokens"]+usage["output_tokens"]+usage["estimated_tokens"] > limits["max_tokens"] or usage["active_seconds"] > limits["max_active_seconds"])
        require(not over or record["state"] in ("ESCALATED","CANCELLED"), "budget", "Over-budget run cannot proceed")
        if record["state"] in ("AWAITING_APPROVAL","COMPLETED"):
            require(record["candidate"] is not None and record["review"] is not None, "approval_scope", "Run has no candidate/review pair")
            candidate, review = self._read(record["candidate"]), self._read(record["review"])
            recommendation = self.validate_review(review,candidate,baseline,record["candidate"],previous_review=previous_review,previous_candidate=previous_candidate)
            require(recommendation == "READY", "not_ready", "Run is not ready for approval")
        if record["state"] == "COMPLETED":
            approval = record["approval"]
            require(approval is not None and approval["decision"] == "APPROVED", "approval", "Completion requires approval")
            require(approval["candidate_digest"] == record["candidate"]["sha256"] and approval["review_digest"] == record["review"]["sha256"], "approval_scope", "Approval covers a different pair")
            require(trusted_final_approval is not None and same(approval,trusted_final_approval), "untrusted_approval", "Completion needs independently verified human approval")
            approved_at = datetime.fromisoformat(approval["timestamp"].replace("Z","+00:00"))
            require(approved_at <= datetime.now(timezone.utc), "approval_time", "Approval is dated in the future")
        # The controller and evaluator must additionally enforce transitions,
        # reservations, request expiry and feature-specific correctness.

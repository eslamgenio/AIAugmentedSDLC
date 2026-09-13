# Local artifact storage and validation

Implemented: immutable local storage, JSON Schema validation, semantic handoff checks, a synthetic command-line demo, the [shipping correctness evaluator](EVALUATION.md) and [creator/reviewer model adapters](AGENT-HANDOFF.md). Application test execution and the durable autonomous workflow controller are not implemented.

## Run on Windows

Prerequisites: Python 3.11 or newer, access to install the declared Python dependencies, and a writable local filesystem supporting hard links, such as NTFS. Run these commands from the project root. The virtual environment stays local and is excluded from Git.

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m sdlc_pilot demo --store outputs/pilot-demo
```

The demo imports the existing synthetic input, A16 and A17 files, verifies their references and validates the illustrative run snapshot. Repeating it against the same store is safe if the example bytes have not changed. A changed file with the same identity/version is rejected, rather than overwritten.

Success means the schemas and handoff relationships pass. The JSON result explicitly reports `human_approved: false`, `agents_executed: false` and `business_correctness_evaluated: false`. This does not approve a real baseline or prove shipping behavior.

For a structural check only:

```powershell
.\.venv\Scripts\python.exe -m sdlc_pilot validate --file docs/pilot/creation.example.json --profile creationBundle --store outputs/pilot-demo --fixture --schema-only
```

For a schema plus semantic handoff check after the demo imports its dependencies:

```powershell
.\.venv\Scripts\python.exe -m sdlc_pilot validate --file docs/pilot/creation.example.json --profile creationBundle --input docs/pilot/input.example.json --store outputs/pilot-demo --fixture
```

Review validation also requires `--candidate-reference`, pointing to a JSON source reference independently selected by the caller. Revision validation takes `--previous-review` and `--previous-candidate` so findings and the new version can be checked against their predecessors. The command returns exit code 0 for success and 1 for a failed check, with a specific error code and message.

## Store behavior

`ArtifactStore.publish_bytes(identity, raw_bytes)` preserves the original serialized bytes. `publish(identity, document)` serializes a dictionary once. Both return a reference containing the identity, schema version and SHA-256 digest. `read(reference)` verifies the digest and metadata before returning the JSON object.

An identity contains project, run, iteration, artifact ID and artifact version. Storage uses an identity-derived directory below `objects/` and the canonical bundle filename. The directory prevents case collisions on Windows and separates runs without trusting caller-supplied paths. There is no mutable `latest` pointer: callers must select an explicit reference.

Publication writes and flushes a temporary file, then creates the final name atomically without replacement. Concurrent writes of identical bytes are idempotent. Concurrent writes of different bytes under the same identity have one winner; the other receives a conflict. There is no unsafe overwrite fallback on filesystems without hard-link support.

After interruption following publication, retrying the same identity and bytes reconciles the existing object without an index repair. A process killed before publication may leave an unreferenced `.pending-*` file; it is not a consumable artifact. No automatic sweeping or deletion of other runs is performed. Power-loss behavior still depends on the filesystem; this is not a replicated durable store.

The store is an integrity primitive, not an approval system. Persisting JSON does not certify its schema or meaning. A future controller must validate before treating an artifact as an accepted handoff. Use an owner-controlled root; the path checks do not defend against a hostile process racing to change filesystem links while a write is in progress.

## Checks implemented

- Strict JSON decoding rejects malformed input, duplicate keys and non-finite numbers.
- Profile schemas reject missing/unknown record fields, invalid canonical child names and malformed timezone-bearing timestamps. The timestamp profile excludes leap seconds.
- Source references resolve to exact stored bytes; missing sources, digest mismatches, scope mismatches and stale inputs are rejected.
- Input validation requires exactly the eight expected upstream sources, unique requirement/criterion/risk IDs, consistent links and the agreed test template.
- Test validation checks unique IDs, requirement/criterion links, matching resource views, automation candidate IDs, child versions and revision context.
- Review validation checks a complete criterion matrix, consistent gaps, valid finding references and JSON-pointer evidence, the pinned current candidate, prior finding dispositions, and READY guards for unresolved findings, blocking questions and exact duplicates.
- Run validation checks pinned input, event ordering/continuity, basic usage limits, current candidate/review references and an independently supplied approval for a completed record. It does not execute transitions or reserve budgets.

The separate shipping evaluator checks expected results and scenario coverage under a restricted test-step template. The wrong-threshold example intentionally passes structural and handoff checks but fails `evaluate`. Arbitrary natural-language test behavior, differently worded duplicate detection and substantive review of resolutions still require further evaluation support and human review.

## Approval and source boundary

Live validation rejects synthetic artifacts by default. Explicit fixture mode accepts only synthetic documents and permits zero upstream digests solely for the fixture input package. Nonzero references must still resolve and match. Fixture-mode success must never authorize a live action.

For live normalized inputs, each upstream source is a stored JSON record with schema_version, synthetic_fixture=false and a payload containing the relevant normalized fields:

| Source | Payload fields checked against the input |
| --- | --- |
| A05 | requirements, baseline_id, baseline_version |
| A04 | acceptance_criteria |
| E09 | approval |
| A15 | test_scope |
| A06 | risks |
| A09 | design_rules |
| E06 | coverage_rules, test_template_fields |
| E01 | business_rules |

This is an adapter projection, not a full schema implementation of those upstream SDLC artifacts.

`PilotValidator(..., trusted_approvals={e09_digest: verified_decision})` requires a matching decision independently supplied by a trusted human-input adapter. The CLI equivalent is `--trusted-approval FILE`, where FILE contains `source_sha256` and `approval`. An actor name inside an agent-produced payload is insufficient. This local implementation does not authenticate humans or verify digital signatures: the application embedding it must control who can configure the trust record. Agents must not populate it.

Final approval is similarly supplied through the library's `trusted_final_approval` argument and must match the candidate and review digests. The CLI deliberately does not provide a command to grant approval or complete a run. Approval expiry, workflow transition rules, model budgets and external authentication belong to the controller step.

## Package and contract maintenance

Source modules live in `sdlc_pilot/`; tests live in `tests/`. The packaged schema is an exact copy of `docs/pilot/contracts.schema.json` so installed code does not depend on the current working directory. A test fails if those copies drift. Update both together when revising the schema version.

Runtime artifacts, virtual environments and packaging output remain excluded from Git. The workbook is unchanged by this implementation.

The [creator/reviewer adapters](AGENT-HANDOFF.md) now run a bounded first-pass handoff through both validation and correctness evaluation. Next: implement the durable controller for corrections, recovery, usage reservations and human approval.

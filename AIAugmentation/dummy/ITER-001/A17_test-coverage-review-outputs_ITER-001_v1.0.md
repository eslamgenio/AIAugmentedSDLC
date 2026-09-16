# A17 — Test Coverage Review Outputs

- **artifact_id:** A17
- **artifact_name:** Test Coverage Review Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** review-test-coverage
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; event/state behavior only
- **Output filename:** `A17_test-coverage-review-outputs_ITER-001_v1.0.md`

## Source references

[requirements.md](requirements.md), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.0.

## Review basis and recommendation

- **Candidate:** [A16_test-case-creation-outputs_ITER-001_v1.0.md](A16_test-case-creation-outputs_ITER-001_v1.0.md), v1.0.
- **baseline_refs:** requirements.md v1.0 and A04 v1.0; A05 baseline v1.0.
- **Recommendation:** REVISE.
- **Rationale:** Multi-device independence has no coverage.
- **Limitations:** Review of the supplied candidate design. Human approval remains pending; no application execution assessed.

## A17-01 — Requirements-to-tests traceability matrix

| req_id | Criterion ID | test_ids | Coverage | Evidence and explanation |
| --- | --- | --- | --- | --- |
| REQ-001 | AC-001 | TC-001 | FULL | steps 1–2 |
| REQ-001 | AC-002 | TC-001 | FULL | step 3 |
| REQ-001 | AC-003 | TC-001 | FULL | step 4 |
| REQ-002 | AC-004 | TC-002 | FULL | steps 2–4 |
| REQ-002 | AC-005 | TC-003 | FULL | step 2 |
| REQ-002 | AC-006 | TC-003 | FULL | steps 2–4 |
| REQ-002 | AC-007 | TC-002 | FULL | steps 1–4 |
| REQ-003 | AC-008 | TC-001 | FULL | step 3 |
| REQ-003 | AC-009 | TC-001 | FULL | step 4 |
| REQ-003 | AC-010 | TC-003 | FULL | step 4 |
| REQ-003 | AC-011 | TC-001, TC-002, TC-003 | FULL | initialization and H checkpoints |
| REQ-004 | AC-012 | None | NONE | No interleaved device events |
| REQ-004 | AC-013 | None | NONE | No second-device notification assertion |

## A17-02 — Coverage gap and duplicate case report

### Gaps

| Gap ID | Requirement / criterion | Missing scenario | Impact | Finding reference |
| --- | --- | --- | --- | --- |
| GAP-001 | REQ-004; AC-012, AC-013 | Interleaved events for DEVICE-A and DEVICE-B | Shared counters or notification suppression could go undetected | F-001 |

### Duplicates

None identified. TC-001 checks the threshold and continuing misses; TC-002 resets a pre-threshold sequence; TC-003 covers recovery and a new incident. Their overlapping setup is useful, distinct coverage.

## A17-03 — Test review findings and revision actions

### F-001 — Missing multi-device independence coverage

- **Severity:** BLOCKING.
- **Affected requirement / criterion IDs:** REQ-004, AC-012 and AC-013.
- **Affected test IDs:** Missing test; all current cases use DEVICE-A only.
- **Evidence:** A16 v1.0 TC-001–003 data and steps contain no DEVICE-B events or assertions. requirements.md REQ-004 requires independently tracked state and notification eligibility.
- **Impact:** The suite cannot detect state leakage, cross-device counter resets or global notification suppression.
- **Requested correction:** Add interleaved two-device scenarios that observe the unaffected device, demonstrate independent miss/reset histories, and require each device to emit its own incident notification. Preserve TC-001–003 and assign new IDs. Do not change requirements or add an API contract.
- **Action owner:** create-test-cases.
- **Disposition:** OPEN.

### Revision actions

| Finding ID | Required action | Owner | Dependency / question | Status |
| --- | --- | --- | --- | --- |
| F-001 | Add tests for AC-012 and AC-013 and update scope accounting | create-test-cases | None; behavior is specified | OPEN |

### Verification of prior findings

Not applicable — initial review. Re-review must inspect the actual new cases before closing F-001.

## Acceptance and handoff

All thirteen criteria are accounted for, including the two uncovered ones. Pass this A17 v1.0 with the exact A16 v1.0 candidate and requirements to create-test-cases for revision. Save the revised A16 as v1.1 and re-review it. REVISE is a design recommendation; no human approval or execution result is supplied.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial review for the v1.0 candidate. |

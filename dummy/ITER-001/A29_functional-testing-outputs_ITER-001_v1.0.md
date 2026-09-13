# A29 — Functional Testing Outputs

- **artifact_id:** A29
- **artifact_name:** Functional Testing Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** execute-functional-tests
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A29_functional-testing-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A16 — Test Case Creation Outputs](A16_test-case-creation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A26 — Test Deployment Outputs](A26_test-deployment-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A04 — Acceptance Criteria Outputs](A04_acceptance-criteria-outputs_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `test_ids` | TC-001, TC-002, TC-003 |
| `req_ids` | REQ-001, REQ-002, REQ-003 |
| `ac_ids` | AC-001–011; AC-012/013 absent |
| `build_id` | B001 |
| `env_id` | LOCAL-TEST |
| `actual` | TC-003 checkpoint 7: OFFLINE; notifications=1 |
| `expected` | TC-003 checkpoint 7: OFFLINE; notifications=2 |
| `status` | TC-001 PASSED; TC-002 PASSED; TC-003 FAILED |
| `evidence` | [native/B001_results.json](native/B001_results.json) |

## A29-01 — Test execution records with actual results

Execution records preserve all checkpoint expectations and actual observations for the three cases.

## A29-02 — Requirement-linked evidence and failure details

TC-003 checkpoint 7 corresponds to A16 TC-003 step 4: a new incident after recovery must emit another notification.

## A29-03 — Defect candidates and blocked-test reasons

Raise DEF-001 against REQ-003 / AC-010. AC-012/013 have no designed cases; do not count them as passed or blocked execution.

## Acceptance and handoff

**Acceptance checks:** Every executed case has actual results. Blocked and not-run cases remain separate.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If incomplete:** Return invalid or incomplete output to execute-functional-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

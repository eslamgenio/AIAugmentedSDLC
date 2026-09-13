# A27 — Smoke Testing Outputs

- **artifact_id:** A27
- **artifact_name:** Smoke Testing Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** execute-smoke-tests
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A27_smoke-testing-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A16 — Test Case Creation Outputs](A16_test-case-creation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A26 — Test Deployment Outputs](A26_test-deployment-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E06 — Test and Defect Baselines](E06_test-and-defect-baselines_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `suite_id` | SMOKE-001 |
| `test_ids` | TC-001 |
| `build_id` | B001 |
| `env_id` | LOCAL-TEST |
| `results` | PASSED for TC-001, from [native/B001_results.json](native/B001_results.json) |
| `failure_evidence` | None for the selected smoke case |
| `recommendation` | Continue diagnosis of functional failure in TC-003; no release recommendation |

## A27-01 — Smoke test results with build and environment IDs

TC-001 is the critical threshold/notification smoke subset and passes on B001.

## A27-02 — Evidence for critical path failures

The smoke result covers one device and one incident; it is not the whole suite.

## A27-03 — Escalation or deeper-testing recommendation

TC-003 failure remains actionable despite smoke passing. Production smoke testing has not occurred.

## Acceptance and handoff

**Acceptance checks:** Critical paths have recorded outcomes. Production scope is distinguished from test scope.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113, H128

**If incomplete:** Return invalid or incomplete output to execute-smoke-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

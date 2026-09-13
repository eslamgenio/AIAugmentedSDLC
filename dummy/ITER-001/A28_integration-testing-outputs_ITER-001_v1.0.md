# A28 — Integration Testing Outputs

- **artifact_id:** A28
- **artifact_name:** Integration Testing Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** execute-integration-tests
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A28_integration-testing-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A09 — System Component Design Outputs](A09_system-component-design-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A16 — Test Case Creation Outputs](A16_test-case-creation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A26 — Test Deployment Outputs](A26_test-deployment-outputs_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `test_ids` | TC-001–003 only as component evidence; no separate integration cases |
| `build_id` | B001 |
| `env_id` | LOCAL-TEST |
| `contract_versions` | A09 v1.0 logical contract |
| `results` | NOT RUN for cross-component integration |
| `requests_responses` | No wire protocol or external response capture supplied |
| `defect_candidates` | None identified from integration execution; execution absent |

## A28-01 — Integration test results with environment details

Integration scope needs an actual adapter/interface contract beyond the in-process component.

## A28-02 — Request, response and event evidence

Component inputs and outputs exist in [native/B001_results.json](native/B001_results.json), but they are not network request/response evidence.

## A28-03 — Defect candidates linked to failing interactions

Report NOT RUN and request the integration boundary before claiming integration coverage.

## Acceptance and handoff

**Acceptance checks:** Interface evidence matches the tested build and contract versions.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If incomplete:** Return invalid or incomplete output to execute-integration-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

# A21 — Code Validation Outputs

- **artifact_id:** A21
- **artifact_name:** Code Validation Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** validate-code
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A21_code-validation-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A20 — Feature Implementation Outputs](A20_feature-implementation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E05 — Repository and CI Evidence](E05_repository-and-ci-evidence_ITER-001_v1.0.md), artifact version 1.0.
- [E03 — Engineering and Governance Policies](E03_engineering-and-governance-policies_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `code_revision` | SRC-001 |
| `test_results` | [native/B001_results.json](native/B001_results.json): TC-001 PASSED; TC-002 PASSED; TC-003 FAILED |
| `coverage` | Three single-device cases; no line-coverage measurement; AC-012/013 untested |
| `static_findings` | NOT RUN; no static analyzer report supplied |
| `tool_versions` | Python standard-library runner RUNNER-001; exact interpreter recorded in [native/runtime.txt](native/runtime.txt) |
| `remediation` | DEF-001: restore eligibility after recovery; rerun component checks and static analysis |

## A21-01 — Unit test results and coverage report

B001 has 2 passing cases and 1 failure. TC-003 reaches the second OFFLINE incident but notification count remains one.

## A21-02 — Static analysis findings with affected locations

Static analysis is NOT RUN, not passing. No measured coverage percentage is supplied.

## A21-03 — Validation summary and remediation actions

Validation is incomplete/failed; correct DEF-001 and obtain missing checks before requesting integration.

## Acceptance and handoff

**Acceptance checks:** All required checks have explicit passed, failed, blocked or not-run status for the same revision.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H065, H068, H075

**If incomplete:** Return invalid or incomplete output to validate-code. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

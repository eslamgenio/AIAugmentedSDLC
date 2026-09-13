# A31 — Regression Testing Outputs

- **artifact_id:** A31
- **artifact_name:** Regression Testing Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** execute-regression-tests
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A31_regression-testing-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A16 — Test Case Creation Outputs](A16_test-case-creation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A35 — Defect Fix Outputs](A35_defect-fix-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A36 — Defect Retest Outputs](A36_defect-retest-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E06 — Test and Defect Baselines](E06_test-and-defect-baselines_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `suite_id` | REGRESSION-001 |
| `selected_test_ids` | TC-001, TC-002, TC-003 |
| `impact_rationale` | Recovery reset may affect threshold, interruption and repeat incidents |
| `build_id` | B002 |
| `results` | 3 PASSED; [native/B002_results.json](native/B002_results.json) |
| `exclusions` | Multi-device scenarios missing from A16 v1.0 |
| `residual_risks` | F-001 remains OPEN; passing existing cases is not full baseline coverage |

## A31-01 — Selected regression scope and selection rationale

Select all three current cases because the fix touches shared event handling.

## A31-02 — Regression results with evidence and build ID

B002 regression has three passing case records; no new failure within that selection.

## A31-03 — New failures, excluded coverage and residual risks

AC-012/013 are excluded by missing design, not by approved scope. Request the A16 revision before declaring adequate coverage.

## Acceptance and handoff

**Acceptance checks:** Selection traces to changes and coverage. Exclusions are explicit.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If incomplete:** Return invalid or incomplete output to execute-regression-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

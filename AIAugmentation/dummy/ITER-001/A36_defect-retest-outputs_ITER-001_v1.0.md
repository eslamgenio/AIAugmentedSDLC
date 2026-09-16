# A36 — Defect Retest Outputs

- **artifact_id:** A36
- **artifact_name:** Defect Retest Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** retest-defects
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A36_defect-retest-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A34 — Defect Triage Outputs](A34_defect-triage-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A35 — Defect Fix Outputs](A35_defect-fix-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A29 — Functional Testing Outputs](A29_functional-testing-outputs_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `defect_id` | DEF-001 |
| `corrected_build_id` | B002 |
| `original_evidence_ref` | [native/B001_results.json](native/B001_results.json) TC-003 checkpoint 7 |
| `retest_steps` | Reset DEVICE-A; send M,M,M,H,M,M,M and observe notification count |
| `result` | PASSED; second incident produces notification 2 |
| `evidence` | [native/B002_results.json](native/B002_results.json) TC-003 checkpoint 7 |
| `recommendation` | Recommend closure after owner confirmation; review and coverage obligations remain |

## A36-01 — Retest execution result and evidence

Retest reproduces the original steps on SRC-002 / B002 and obtains two notifications.

## A36-02 — Fix verification linked to defect and build

Match both the defect and corrected build; B001 remains the failing historical evidence.

## A36-03 — Closure or reopening recommendation

Recommend closure of DEF-001 only; do not conclude all release risks are resolved.

## Acceptance and handoff

**Acceptance checks:** Retest uses the corrected build. Closure is only a recommendation until owner confirmation.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If incomplete:** Return invalid or incomplete output to retest-defects. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

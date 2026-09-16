# A35 — Defect Fix Outputs

- **artifact_id:** A35
- **artifact_name:** Defect Fix Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** fix-defects
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A35_defect-fix-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A34 — Defect Triage Outputs](A34_defect-triage-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A20 — Feature Implementation Outputs](A20_feature-implementation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A22 — Code Review Outputs](A22_code-review-outputs_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `defect_id` | DEF-001 |
| `root_cause` | notified set retained DEVICE-A after recovery |
| `changed_revision` | SRC-002 |
| `test_refs` | [native/test_scenarios.json](native/test_scenarios.json) TC-003; full runner also covers TC-001/002 |
| `validation_refs` | [native/B002_results.json](native/B002_results.json); [native/build-records.json](native/build-records.json) |
| `review_package` | [native/monitor_SRC-002.py](native/monitor_SRC-002.py) versus [native/monitor_SRC-001.py](native/monitor_SRC-001.py); review pending |

## A35-01 — Proposed fix and root cause explanation

The received-heartbeat branch now discards DEVICE-A from the notified set, allowing the next incident to notify.

## A35-02 — Unit or regression tests for the defect

TC-003 supplies regression protection for the reproduced failure; its original ID is retained.

## A35-03 — Validation evidence and change review package

B002 passes all three current cases. Submit SRC-002 for review; passing tests do not close CR-001 or F-001 automatically.

## Acceptance and handoff

**Acceptance checks:** Fix addresses the reproduced failure and includes regression protection. Review is still required.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H061, H064, H067, H076, H092

**If incomplete:** Return invalid or incomplete output to fix-defects. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

# A20 — Feature Implementation Outputs

- **artifact_id:** A20
- **artifact_name:** Feature Implementation Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** implement-feature
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A20_feature-implementation-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A11 — Work Breakdown Outputs](A11_work-breakdown-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A09 — System Component Design Outputs](A09_system-component-design-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E05 — Repository and CI Evidence](E05_repository-and-ci-evidence_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `code_revision` | SRC-001 |
| `diff_ref` | [native/monitor_SRC-001.py](native/monitor_SRC-001.py); initial implementation against A09 |
| `work_id` | W-001, W-002; W-003 pending |
| `req_ids` | REQ-001–004 |
| `unit_test_refs` | [native/run_cases.py](native/run_cases.py); [native/test_scenarios.json](native/test_scenarios.json) |
| `change_summary` | Added keyed state, event handling and notification tracking |
| `limitations` | Recovery notification eligibility requires review; no API, persistence or production integration |

## A20-01 — Feature code and associated unit tests

Feature source is [native/monitor_SRC-001.py](native/monitor_SRC-001.py); the three component cases are in the local runner.

## A20-02 — Change summary and implementation notes

Register initializes ONLINE state. Misses increment a device counter; received heartbeats reset state.

## A20-03 — Known limitations and review questions

Review whether the notified set follows incident lifetime. Unknown events are outside accepted scope even though the local adapter rejects them.

## Acceptance and handoff

**Acceptance checks:** Change links to its task and criteria. Unit tests and limitations are supplied.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H061, H064, H067, H092

**If incomplete:** Return invalid or incomplete output to implement-feature. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

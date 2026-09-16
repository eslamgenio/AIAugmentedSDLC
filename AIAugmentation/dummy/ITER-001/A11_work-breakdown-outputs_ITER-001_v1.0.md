# A11 — Work Breakdown Outputs

- **artifact_id:** A11
- **artifact_name:** Work Breakdown Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** decompose-work
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A11_work-breakdown-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A03 — Requirements Analysis Outputs](A03_requirements-analysis-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A04 — Acceptance Criteria Outputs](A04_acceptance-criteria-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A09 — System Component Design Outputs](A09_system-component-design-outputs_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `items[{work_id,req_ids,ac_ids,tasks,dependencies,done_criteria}]` | W-001: REQ-001/002, AC-001–007, implement keyed status/reset, no dependency, done when transitions pass; W-002: REQ-003, AC-008–011, implement notification lifecycle, depends W-001, done when incidents notify exactly once; W-003: REQ-004, AC-012/013, validate isolation, depends W-001/002, done when interleaved tests pass |
| `estimates_pending` | See A12 estimates; team agreement pending |

## A11-01 — Epics, stories and actionable task breakdown

W-001 builds state handling; W-002 notification lifecycle; W-003 proves device isolation.

## A11-02 — Requirement-to-work-item links

Each work item links to its requirement and criteria in the Required content record.

## A11-03 — Dependencies and completion criteria per item

Completion requires relevant tests, review and no blocking findings. W-003 cannot be declared complete from single-device tests.

## Acceptance and handoff

**Acceptance checks:** Tasks are scoped and traceable. Completion criteria and dependencies are present.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H034, H037, H040, H058, H132

**If incomplete:** Return invalid or incomplete output to decompose-work. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

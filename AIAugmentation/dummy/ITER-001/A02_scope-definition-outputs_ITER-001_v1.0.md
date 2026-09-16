# A02 — Scope Definition Outputs

- **artifact_id:** A02
- **artifact_name:** Scope Definition Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** define-scope
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A02_scope-definition-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A01 — Requirements Elicitation Outputs](A01_requirements-elicitation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E01 — Business Context](E01_business-context_ITER-001_v1.0.md), artifact version 1.0.
- [E09 — Human Decisions](E09_human-decisions_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `scope_id` | SCOPE-001 |
| `included` | REQ-001–004: status, miss counter and incident notifications |
| `excluded` | Registration, malformed events, timing, transport, persistence and performance |
| `goals[{metric,target}]` | metric=notifications per offline incident; target=1; metric=miss threshold; target=3 |
| `constraints` | Ordered valid events; no network delivery promise |
| `agreement_status` | PENDING; E09 DEC-001 |

## A02-01 — Scope statement with inclusions and exclusions

Include only the event/state behavior in requirements.md. Exclusions apply to all downstream assessments.

## A02-02 — Business goals and success measures

Success means the third miss changes state and emits one device-specific notification, with a new notification after recovery and a subsequent incident.

## A02-03 — Constraints, assumptions and agreement checklist

Confirm baseline agreement through E09; do not interpret design feasibility as approval.

## Acceptance and handoff

**Acceptance checks:** Scope boundaries and measurable goals are consistent. Agreement is not inferred.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H007, H009, H013, H018, H118, H131

**If incomplete:** Return invalid or incomplete output to define-scope. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

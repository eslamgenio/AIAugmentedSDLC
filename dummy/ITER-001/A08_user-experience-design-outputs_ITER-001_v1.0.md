# A08 — User Experience Design Outputs

- **artifact_id:** A08
- **artifact_name:** User Experience Design Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** design-user-experience
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A08_user-experience-design-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A05 — Requirements Review Outputs](A05_requirements-review-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E02 — Product and Architecture Context](E02_product-and-architecture-context_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `journeys` | Operator inspects device status, investigates OFFLINE, and observes ONLINE after recovery |
| `user_roles` | IoT operations engineer |
| `UI_states` | ONLINE and OFFLINE; loading/error UI unspecified |
| `wireframe_refs` | No committed UI; proposed text layout in A08-02 |
| `accessibility_checks` | Not assessed; no interactive UI supplied |
| `questions` | UX-Q01: should a future dashboard show incident history? Product owner; future scope only |

## A08-01 — User journeys and interaction flows

Operator identifies DEVICE-A as OFFLINE and consults its notification record; recovery restores ONLINE.

## A08-02 — Wireframes or prototype specifications

Proposed read-only layout: Device ID / Connection status / Notification history. This is a discussion sketch, not an accepted UI contract.

## A08-03 — Usability review questions and UI state definitions

Both states must be distinguishable by text, not color alone if a UI is later designed. UI loading, authentication and navigation require separate requirements.

## Acceptance and handoff

**Acceptance checks:** Journeys cover normal, error and recovery states for the agreed users.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H028

**If incomplete:** Return invalid or incomplete output to design-user-experience. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

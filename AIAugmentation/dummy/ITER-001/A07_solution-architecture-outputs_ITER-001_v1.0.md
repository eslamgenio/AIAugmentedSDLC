# A07 — Solution Architecture Outputs

- **artifact_id:** A07
- **artifact_name:** Solution Architecture Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** design-solution-architecture
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A07_solution-architecture-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A05 — Requirements Review Outputs](A05_requirements-review-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A06 — Feasibility Assessment Outputs](A06_feasibility-assessment-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A09 — System Component Design Outputs](A09_system-component-design-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E02 — Product and Architecture Context](E02_product-and-architecture-context_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `components` | Event adapter; per-device monitor; notification log |
| `interfaces` | Registered device ID plus HEARTBEAT_MISSED or HEARTBEAT_RECEIVED; status and notification outputs |
| `deployment_view` | Single in-process component; no network topology committed |
| `decisions[{adr_id,rationale}]` | ADR-001: dictionary keyed by device ID prevents shared counters; ADR-002: incident eligibility resets on recovery |
| `req_links` | REQ-001/002 monitor; REQ-003 log; REQ-004 keyed state |

## A07-01 — Architecture diagrams and component responsibilities

Event adapter → per-device monitor → notification log. Adapter supplies valid ordered events; monitor owns counts and status.

## A07-02 — Architecture decision records

ADR-001 separates device state. ADR-002 requires recovery to re-enable the next incident notification. A09 is the logical interface source.

## A07-03 — Deployment view and requirement traceability

Deployable topology remains undecided. A local adapter is supplied later for exercising the component; no HTTP API is added to the requirements.

## Acceptance and handoff

**Acceptance checks:** Architecture traces to the reviewed baseline and records important tradeoffs.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H025, H028, H032, H037, H043, H059, H066, H104

**If incomplete:** Return invalid or incomplete output to design-solution-architecture. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

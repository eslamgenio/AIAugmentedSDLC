# A01 — Requirements Elicitation Outputs

- **artifact_id:** A01
- **artifact_name:** Requirements Elicitation Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** elicit-requirements
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A01_requirements-elicitation-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [E01 — Business Context](E01_business-context_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `needs[{need_id,source,user,problem}]` | NEED-001: source E01 BUSINESS-001; user IoT operations engineer; problem repeated offline alerts obscure real incidents |
| `requirements[{req_id,scenario}]` | REQ-001: detect three consecutive misses; REQ-002: reset and recover; REQ-003: one notification per incident; REQ-004: independent devices |
| `questions[{owner,status}]` | No in-scope questions; product owner unassigned; agreement PENDING |

## A01-01 — Stakeholder needs register with source links

NEED-001 links to E01 and the Goal in requirements.md v1.0.

## A01-02 — Draft requirements and user scenarios

Draft scenarios: lose connection after three misses, recover on heartbeat, then create a fresh incident; interleave DEVICE-A and DEVICE-B. Requirement text remains authoritative in requirements.md.

## A01-03 — Open questions and assumptions log

Assumption: events are valid, ordered and delivered once. Timing and transport are excluded. No open behavior questions; stakeholder agreement is pending.

## Acceptance and handoff

**Acceptance checks:** Every need has evidence and an owner. Assumptions remain explicit.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H004, H007, H011, H022, H109

**If incomplete:** Return invalid or incomplete output to elicit-requirements. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

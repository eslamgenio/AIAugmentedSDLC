# E08 — Operational and Product Evidence

- **artifact_id:** E08
- **artifact_name:** Operational and Product Evidence
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** Observability, support and research systems
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `E08_operational-and-product-evidence_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- Owner/context record is supplied directly in this artifact; no external owner decision is inferred.

## Required content

| Field | Value / evidence |
| --- | --- |
| `source_id` | SUPPORT-BASELINE-001 |
| `service_version` | Not supplied; no claim of current production deployment |
| `environment` | Product research context |
| `observation_period` | 2026-09-12 09:00–10:00 UTC |
| `ticket_ids` | SUPPORT-001 |
| `events` | Operator request: show prior offline incidents per device to aid investigation |
| `units` | One request; no prevalence or latency measurement |
| `evidence_refs` | SUPPORT-001 record in this document |

## Supporting records

SUPPORT-001: IoT operations role requests a read-only incident history. Device, account and service telemetry are not supplied. Treat this as feedback, not evidence of a service outage.

## Acceptance and handoff

**Acceptance checks:** Telemetry is current for the relevant version and window. Units and known gaps are recorded.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H090, H100, H101, H104, H127, H128, H130, H131

**If incomplete:** Request correction or a current record from Observability, support and research systems. Keep dependent work blocked until the required evidence or permission is supplied.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

# A09 — System Component Design Outputs

- **artifact_id:** A09
- **artifact_name:** System Component Design Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.1
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** design-system-components
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** the embedded A05-02 baseline v1.0; event/state behavior only
- **Output filename:** `A09_system-component-design-outputs_ITER-001_v1.1.md`

## Source references

[A05-02 baseline](A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02-proposed-baseline-with-revision-history), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.1.

## Required content

| Field | Value / section reference |
| --- | --- |
| `API_contract_refs` | A09-01 logical contract v1.0; no concrete endpoint supplied |
| `schemas` | A09-02 conceptual model v1.0; wire schema not specified |
| `validation_rules` | Ordered valid events for registered devices only; see A09-03 |
| `error_behaviors` | Malformed/duplicate events and transport failures excluded |
| `data_ownership` | Independent state and notifications per registered device |
| `migrations` | Not applicable; persistence excluded |

## A09-01 — API and integration contract drafts

Logical contract only; no HTTP endpoint, transport, payload serialization or UI is specified.

- Input: a registered device identifier and one event, HEARTBEAT_RECEIVED or HEARTBEAT_MISSED.
- Process each event once in supplied order.
- Observable output: the device's current ONLINE/OFFLINE status and emitted offline-notification records identifying the affected device.
- The upstream detector decides whether a heartbeat was missed; this component does not calculate elapsed time.

## A09-02 — Data model and migration considerations

| Logical item | Meaning |
| --- | --- |
| device_id | Identifier of an already registered device; independent state is maintained per identifier. |
| status | ONLINE or OFFLINE; initially ONLINE. |
| consecutive_misses | Per-device count, initially zero. |
| offline notification | Record identifying the device for one ONLINE-to-OFFLINE transition. |

These are conceptual names, not a new wire schema. Persistence, database design and migrations are outside scope.

## A09-03 — Component behavior and failure-handling specifications

1. For HEARTBEAT_RECEIVED, reset that device's miss count to zero and set it ONLINE. Emit no offline notification.
2. For HEARTBEAT_MISSED, increment that device's miss count. At a count of three or more it is OFFLINE; below three it remains ONLINE.
3. Emit exactly one offline notification only when this processing changes that device from ONLINE to OFFLINE. No notification is emitted while it remains OFFLINE.
4. Leave all other devices' state, counters and notification eligibility unchanged.

This restates REQ-001 through REQ-004. Unknown devices, malformed/duplicate events and notification-delivery failures are excluded by the embedded A05-02 baseline. No error code or recovery policy is invented for them.

## Acceptance and handoff

Draft input for test design/review. Scope and source versions are explicit. Human agreement remains PENDING in E09; no approval gate is satisfied. Environment readiness is unverified and execution is outside scope. Correct any newly identified source conflict before relying on the affected behavior.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

# E01 — Business Context

- **artifact_id:** E01
- **artifact_name:** Business Context
- **iteration_id:** ITER-001
- **artifact_version:** 1.1
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** Business and product owners
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** the embedded A05-02 baseline v1.0; event/state behavior only
- **Output filename:** `E01_business-context_ITER-001_v1.1.md`

## Source references

[A05-02 baseline](A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02-proposed-baseline-with-revision-history), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.1.

## Required content

| Field | Value / section reference |
| --- | --- |
| `source_id` | BUSINESS-001 |
| `owner` | Product owner role; unassigned |
| `date` | 2026-09-13 preparation date |
| `goals` | Identify offline devices without repeated incident alerts |
| `constraints` | Event/state rules only; see the embedded A05-02 baseline scope |
| `scenarios` | Loss of connection, recovery, repeated incidents, independent devices |
| `business_rules` | See Business rules and workflow |
| `evidence_links` | the embedded A05-02 baseline v1.0; supplied example, not interviews or telemetry |

## Business context

Source ID: BUSINESS-001. Owner: Product owner (unassigned). Context version: 1.0.

IoT operations engineers need to identify disconnected devices while avoiding repeated alerts during one continuous offline incident.

## Business rules and workflow

- A registered device initially appears ONLINE.
- Three consecutive missed heartbeats indicate lost connectivity; one received heartbeat restores ONLINE and resets the sequence.
- An offline incident has one notification identifying its device. Recovery permits a notification for a later incident.
- Device monitoring and notifications are independent across devices.
- Operations can inspect status and notification records to determine which device needs investigation.

## Goals and constraints

The objective is correct state/notification behavior, not a response-time or delivery-channel commitment. Use only the event ordering and functional scope defined in the embedded A05-02 baseline. No interviews, user research, cost savings or production telemetry are claimed.

No unresolved behavior questions have been identified within the stated scope. Owner agreement is pending in E09.

## Acceptance and handoff

Draft input for test design/review. Scope and source versions are explicit. Human agreement remains PENDING in E09; no approval gate is satisfied. Environment readiness is unverified and execution is outside scope. Correct any newly identified source conflict before relying on the affected behavior.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

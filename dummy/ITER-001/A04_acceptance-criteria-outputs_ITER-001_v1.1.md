# A04 — Acceptance Criteria Outputs

- **artifact_id:** A04
- **artifact_name:** Acceptance Criteria Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.1
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** define-acceptance-criteria
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** the embedded A05-02 baseline v1.0; event/state behavior only
- **Output filename:** `A04_acceptance-criteria-outputs_ITER-001_v1.1.md`

## Source references

[A05-02 baseline](A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02-proposed-baseline-with-revision-history), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.1.

## Required content

| Field | Value / section reference |
| --- | --- |
| `boundary_questions` | None within scope; see A04-03. |

### criteria records

| ac_id | req_id | precondition | action | expected |
| --- | --- | --- | --- | --- |
| AC-001 | REQ-001 | State and history specified in AC-001 | Process the source-defined event sequence | With zero, one or two consecutive missed heartbeats, a device that started ONLINE remains ONLINE. |
| AC-002 | REQ-001 | State and history specified in AC-002 | Process the source-defined event sequence | The third consecutive missed heartbeat changes that device to OFFLINE. |
| AC-003 | REQ-001 | State and history specified in AC-003 | Process the source-defined event sequence | Further missed heartbeats keep the device OFFLINE. |
| AC-004 | REQ-002 | State and history specified in AC-004 | Process the source-defined event sequence | A received heartbeat interrupts a sequence of misses; misses before that heartbeat do not count toward a later offline transition. |
| AC-005 | REQ-002 | State and history specified in AC-005 | Process the source-defined event sequence | A received heartbeat restores an OFFLINE device to ONLINE immediately when the event is processed. |
| AC-006 | REQ-002 | State and history specified in AC-006 | Process the source-defined event sequence | After recovery, three new consecutive misses are required to make the device OFFLINE again. |
| AC-007 | REQ-002 | State and history specified in AC-007 | Process the source-defined event sequence | A received heartbeat for an already ONLINE device keeps it ONLINE and resets the count to zero. |
| AC-008 | REQ-003 | State and history specified in AC-008 | Process the source-defined event sequence | The transition on the third consecutive miss emits one notification for that device. |
| AC-009 | REQ-003 | State and history specified in AC-009 | Process the source-defined event sequence | Additional misses during the same offline incident emit no additional notifications. |
| AC-010 | REQ-003 | State and history specified in AC-010 | Process the source-defined event sequence | After recovery, a new offline incident emits one new notification. |
| AC-011 | REQ-003 | State and history specified in AC-011 | Process the source-defined event sequence | Initialization and HEARTBEAT_RECEIVED events emit no offline notifications. Recovery notifications are not part of this feature. |
| AC-012 | REQ-004 | State and history specified in AC-012 | Process the source-defined event sequence | Events for one device do not change another device's status or miss count. |
| AC-013 | REQ-004 | State and history specified in AC-013 | Process the source-defined event sequence | Notifications for one device do not suppress notifications for another device's offline incident. |

## A04-01 — Requirement-linked acceptance criteria

The source statements below are preserved verbatim. Their IDs remain authoritative for the generated test cases.

| Requirement | Criterion | Observable acceptance behavior |
| --- | --- | --- |
| REQ-001 | AC-001 | With zero, one or two consecutive missed heartbeats, a device that started ONLINE remains ONLINE. |
| REQ-001 | AC-002 | The third consecutive missed heartbeat changes that device to OFFLINE. |
| REQ-001 | AC-003 | Further missed heartbeats keep the device OFFLINE. |
| REQ-002 | AC-004 | A received heartbeat interrupts a sequence of misses; misses before that heartbeat do not count toward a later offline transition. |
| REQ-002 | AC-005 | A received heartbeat restores an OFFLINE device to ONLINE immediately when the event is processed. |
| REQ-002 | AC-006 | After recovery, three new consecutive misses are required to make the device OFFLINE again. |
| REQ-002 | AC-007 | A received heartbeat for an already ONLINE device keeps it ONLINE and resets the count to zero. |
| REQ-003 | AC-008 | The transition on the third consecutive miss emits one notification for that device. |
| REQ-003 | AC-009 | Additional misses during the same offline incident emit no additional notifications. |
| REQ-003 | AC-010 | After recovery, a new offline incident emits one new notification. |
| REQ-003 | AC-011 | Initialization and HEARTBEAT_RECEIVED events emit no offline notifications. Recovery notifications are not part of this feature. |
| REQ-004 | AC-012 | Events for one device do not change another device's status or miss count. |
| REQ-004 | AC-013 | Notifications for one device do not suppress notifications for another device's offline incident. |

## A04-02 — Given/When/Then scenarios where useful

- Given an ONLINE device with two consecutive misses, when HEARTBEAT_MISSED is processed, then it becomes OFFLINE and one notification identifies that device. Links: AC-002, AC-008.
- Given an OFFLINE device, when HEARTBEAT_RECEIVED is processed, then it becomes ONLINE, the miss count resets to zero, and no offline notification is emitted. Links: AC-005, AC-011.
- Given devices A and B, when an event for A is processed, then B's state and miss count are unchanged. Link: AC-012.

These examples illustrate the criteria; they do not replace full test design.

## A04-03 — Unresolved examples and boundary questions

None within the stated scope. Zero, one and two misses remain ONLINE; three cause OFFLINE; further misses do not repeat the notification. Do not request timing, malformed-event or delivery-retry rules for this feature because they are explicitly excluded.

## Acceptance and handoff

Draft input for test design/review. Scope and source versions are explicit. Human agreement remains PENDING in E09; no approval gate is satisfied. Environment readiness is unverified and execution is outside scope. Correct any newly identified source conflict before relying on the affected behavior.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

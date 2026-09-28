# A04 - Acceptance Criteria Outputs

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.1

**Status:** Draft supporting input, based on the embedded A05-02 baseline version 1.0.

Source: [A05-02 baseline](A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02--proposed-baseline-with-revision-history), feature version 1.0.

## A04-01 - Requirement-linked acceptance criteria

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

## A04-02 - Given/When/Then scenarios where useful

- Given an ONLINE device with two consecutive misses, when HEARTBEAT_MISSED is processed, then it becomes OFFLINE and one notification identifies that device. Links: AC-002, AC-008.
- Given an OFFLINE device, when HEARTBEAT_RECEIVED is processed, then it becomes ONLINE, the miss count resets to zero, and no offline notification is emitted. Links: AC-005, AC-011.
- Given devices A and B, when an event for A is processed, then B's state and miss count are unchanged. Link: AC-012.

These features illustrate the criteria; they do not replace full test design.

## A04-03 - Unresolved features and boundary questions

None within the stated scope. Zero, one and two misses remain ONLINE; three cause OFFLINE; further misses do not repeat the notification. Do not request timing, malformed-event or delivery-retry rules for this feature because they are explicitly excluded.

## Revision history

| Artifact version | Change |
| --- | --- |
| 1.0 | Initial artifact retained unchanged. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

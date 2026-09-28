# A05 — Requirements Review Outputs

- **artifact_id:** A05
- **artifact_name:** Requirements Review Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.1
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** review-requirements
- **Document status:** DRAFT; stakeholder approval PENDING
- **Scope:** Complete event/state baseline embedded in A05-02.
- **Output filename:** `A05_requirements-review-outputs_ITER-001_v1.1.md`

## Source references

This artifact embeds the complete DEVICE-CONNECTION-BASELINE v1.0. Requirement behavior, IDs and scope are unchanged; artifact version 1.1 consolidates the previously separate baseline text. No separate requirements document is needed to consume this version.

## Required content

| Field | Value / section reference |
| --- | --- |
| `baseline_id` | DEVICE-CONNECTION-BASELINE v1.0 |
| `req_versions` | Embedded REQ-001–004 and AC-001–013, behavior version 1.0, in A05-02 |
| `review_findings` | A05-01, RR-001–003 |
| `actions` | Preserve source boundaries and include interleaved device coverage |
| `stakeholder_decision_refs` | E09 v1.1, DEC-001, PENDING |

## A05-01 — Requirements review findings and actions

| Finding | Assessment | Disposition |
| --- | --- | --- |
| RR-001 | Threshold, initial state, reset and notification rules are explicit. | No behavior change proposed. |
| RR-002 | Events are ordered and processed once; timing and transport are excluded. | Preserve these boundaries. |
| RR-003 | Device state and notification independence are required. | Include interleaved device scenarios. |

Review sign-off remains pending.

## A05-02 — Proposed baseline with revision history

**Baseline ID:** DEVICE-CONNECTION-BASELINE. **Behavior version:** 1.0.

The following is the complete baseline. A04 v1.1 restates its acceptance criteria. Flag discrepancies in supporting artifacts instead of silently inventing or selecting different behavior.

### Goal

As an IoT operations engineer, I want to see when a device loses its connection and receive one notification for each offline incident, so that I can investigate without receiving repeated alerts for the same incident.

### Context and terminology

- Each registered device starts ONLINE with a consecutive-miss count of zero.
- The monitoring component receives an ordered sequence of events for each device: HEARTBEAT_RECEIVED or HEARTBEAT_MISSED.
- HEARTBEAT_RECEIVED means a valid heartbeat arrived. HEARTBEAT_MISSED means the upstream heartbeat detector reported one missed heartbeat.
- Process each event once, in the supplied order. Timing and heartbeat detection are outside this feature's scope.
- Observable outputs are each device's ONLINE/OFFLINE status and a log of emitted offline notifications, including the device ID.
- An offline incident starts when a device changes from ONLINE to OFFLINE and ends when it returns ONLINE.

### REQ-001: Detect a lost connection

For each device, increment its consecutive-miss count by one for each HEARTBEAT_MISSED event. Change its status to OFFLINE when the count reaches three.

- **AC-001:** With zero, one or two consecutive missed heartbeats, a device that started ONLINE remains ONLINE.
- **AC-002:** The third consecutive missed heartbeat changes that device to OFFLINE.
- **AC-003:** Further missed heartbeats keep the device OFFLINE.

### REQ-002: Reset the count and recover

A HEARTBEAT_RECEIVED event resets that device's consecutive-miss count to zero and sets its status to ONLINE.

- **AC-004:** A received heartbeat interrupts a sequence of misses; misses before that heartbeat do not count toward a later offline transition.
- **AC-005:** A received heartbeat restores an OFFLINE device to ONLINE immediately when the event is processed.
- **AC-006:** After recovery, three new consecutive misses are required to make the device OFFLINE again.
- **AC-007:** A received heartbeat for an already ONLINE device keeps it ONLINE and resets the count to zero.

### REQ-003: Notify once per offline incident

Emit exactly one offline notification when a device changes from ONLINE to OFFLINE. The notification identifies the affected device.

- **AC-008:** The transition on the third consecutive miss emits one notification for that device.
- **AC-009:** Additional misses during the same offline incident emit no additional notifications.
- **AC-010:** After recovery, a new offline incident emits one new notification.
- **AC-011:** Initialization and HEARTBEAT_RECEIVED events emit no offline notifications. Recovery notifications are not part of this feature.

### REQ-004: Keep device state independent

Track connection state and consecutive misses separately for each registered device.

- **AC-012:** Events for one device do not change another device's status or miss count.
- **AC-013:** Notifications for one device do not suppress notifications for another device's offline incident.

### Test-design scope

Cover normal operation, the missed-heartbeat threshold, interruption of consecutive misses, recovery, repeated incidents, notification suppression and interleaved events for multiple devices. Choose enough distinct scenarios to demonstrate the behavior; no fixed test count is required.

For test design, assume a test environment can reset registered devices, submit the two event types and inspect device status and notification records. No specific API, command or UI is prescribed.

Out of scope: device registration, unknown devices, malformed or duplicate events, heartbeat scheduling, network transport, notification delivery channels/retries, authentication, persistence across restarts and performance targets.

### Input completeness

There are no known unresolved behavior questions within the stated scope. If you identify a conflict or a missing rule needed for an expected result, record a question rather than inventing a rule. Do not treat an explicitly excluded feature as a mandatory coverage gap.

## A05-03 — Agreement record with pending decisions

[E09 v1.1](../External%20Inputs/E09_human-decisions_ITER-001_v1.1.md) records DEC-001 as PENDING against this artifact revision. No stakeholder approval is claimed. Consolidation changes packaging only; new decisions must still identify their exact artifact revision.

## Acceptance and handoff

All four requirements, thirteen acceptance criteria, terminology, initial state, scope exclusions and input-completeness notes are present in A05-02. Draft test design may proceed; this document does not grant human approval. Consumers reference this exact A05 v1.1 and applicable supporting versions.

## Revision history

| Artifact version | Baseline behavior version | Change |
| --- | --- | --- |
| 1.0 | 1.0 | Referenced a separately stored baseline. |
| 1.1 | 1.0 | Embedded the complete baseline without changing behavior or IDs; prior artifact retained. |

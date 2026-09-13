# Example requirements: IoT device connection monitoring

**Feature ID:** DEVICE-CONNECTION
**Version:** 1.0
**Status:** Synthetic example for testing the test-case creation and coverage-review skills. No real product approval is implied.

## Goal

As an IoT operations engineer, I want to see when a device loses its connection and receive one notification for each offline incident, so that I can investigate without receiving repeated alerts for the same incident.

## Context and terminology

- Each registered device starts ONLINE with a consecutive-miss count of zero.
- The monitoring component receives an ordered sequence of events for each device: HEARTBEAT_RECEIVED or HEARTBEAT_MISSED.
- HEARTBEAT_RECEIVED means a valid heartbeat arrived. HEARTBEAT_MISSED means the upstream heartbeat detector reported one missed heartbeat.
- Process each event once, in the supplied order. Timing and heartbeat detection are outside this feature's scope.
- Observable outputs are each device's ONLINE/OFFLINE status and a log of emitted offline notifications, including the device ID.
- An offline incident starts when a device changes from ONLINE to OFFLINE and ends when it returns ONLINE.

## REQ-001: Detect a lost connection

For each device, increment its consecutive-miss count by one for each HEARTBEAT_MISSED event. Change its status to OFFLINE when the count reaches three.

- **AC-001:** With zero, one or two consecutive missed heartbeats, a device that started ONLINE remains ONLINE.
- **AC-002:** The third consecutive missed heartbeat changes that device to OFFLINE.
- **AC-003:** Further missed heartbeats keep the device OFFLINE.

## REQ-002: Reset the count and recover

A HEARTBEAT_RECEIVED event resets that device's consecutive-miss count to zero and sets its status to ONLINE.

- **AC-004:** A received heartbeat interrupts a sequence of misses; misses before that heartbeat do not count toward a later offline transition.
- **AC-005:** A received heartbeat restores an OFFLINE device to ONLINE immediately when the event is processed.
- **AC-006:** After recovery, three new consecutive misses are required to make the device OFFLINE again.
- **AC-007:** A received heartbeat for an already ONLINE device keeps it ONLINE and resets the count to zero.

## REQ-003: Notify once per offline incident

Emit exactly one offline notification when a device changes from ONLINE to OFFLINE. The notification identifies the affected device.

- **AC-008:** The transition on the third consecutive miss emits one notification for that device.
- **AC-009:** Additional misses during the same offline incident emit no additional notifications.
- **AC-010:** After recovery, a new offline incident emits one new notification.
- **AC-011:** Initialization and HEARTBEAT_RECEIVED events emit no offline notifications. Recovery notifications are not part of this feature.

## REQ-004: Keep device state independent

Track connection state and consecutive misses separately for each registered device.

- **AC-012:** Events for one device do not change another device's status or miss count.
- **AC-013:** Notifications for one device do not suppress notifications for another device's offline incident.

## Test-design scope

Cover normal operation, the missed-heartbeat threshold, interruption of consecutive misses, recovery, repeated incidents, notification suppression and interleaved events for multiple devices. Choose enough distinct scenarios to demonstrate the behavior; no fixed test count is required.

For test design, assume a test environment can reset registered devices, submit the two event types and inspect device status and notification records. No specific API, command or UI is prescribed.

Out of scope: device registration, unknown devices, malformed or duplicate events, heartbeat scheduling, network transport, notification delivery channels/retries, authentication, persistence across restarts and performance targets.

## Input completeness

There are no intentionally unresolved behavior questions within this example's scope. If you identify a conflict or a missing rule needed for an expected result, record a question rather than inventing a rule. Do not treat an explicitly excluded feature as a mandatory coverage gap.

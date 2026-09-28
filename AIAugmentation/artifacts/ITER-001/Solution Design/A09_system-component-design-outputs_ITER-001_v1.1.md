# A09 - System Component Design Outputs

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.1

**Status:** Draft supporting input, based on the embedded A05-02 baseline version 1.0.

Source: [A05-02 baseline](../Requirements/A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02--proposed-baseline-with-revision-history), feature version 1.0.

## A09-01 - API and integration contract drafts

Logical contract only; no HTTP endpoint, transport, payload serialization or UI is specified.

- Input: a registered device identifier and one event, HEARTBEAT_RECEIVED or HEARTBEAT_MISSED.
- Process each event once in supplied order.
- Observable output: the device's current ONLINE/OFFLINE status and emitted offline-notification records identifying the affected device.
- The upstream detector decides whether a heartbeat was missed; this component does not calculate elapsed time.

## A09-02 - Data model and migration considerations

| Logical item | Meaning |
| --- | --- |
| device_id | Identifier of an already registered device; independent state is maintained per identifier. |
| status | ONLINE or OFFLINE; initially ONLINE. |
| consecutive_misses | Per-device count, initially zero. |
| offline notification | Record identifying the device for one ONLINE-to-OFFLINE transition. |

These are conceptual names, not a new wire schema. Persistence, database design and migrations are outside scope.

## A09-03 - Component behavior and failure-handling specifications

1. For HEARTBEAT_RECEIVED, reset that device's miss count to zero and set it ONLINE. Emit no offline notification.
2. For HEARTBEAT_MISSED, increment that device's miss count. At a count of three or more it is OFFLINE; below three it remains ONLINE.
3. Emit exactly one offline notification only when this processing changes that device from ONLINE to OFFLINE. No notification is emitted while it remains OFFLINE.
4. Leave all other devices' state, counters and notification eligibility unchanged.

This restates REQ-001 through REQ-004. Unknown devices, malformed/duplicate events and notification-delivery failures are excluded by the embedded A05-02 baseline. No error code or recovery policy is invented for them.

## Revision history

| Artifact version | Change |
| --- | --- |
| 1.0 | Initial artifact retained unchanged. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

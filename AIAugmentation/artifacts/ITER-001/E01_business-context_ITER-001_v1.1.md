# E01 - Business Context

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.1

**Status:** Draft supporting input, based on the embedded A05-02 baseline version 1.0.

Source: [A05-02 baseline](A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02-proposed-baseline-with-revision-history), feature version 1.0.

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

## Revision history

| Artifact version | Change |
| --- | --- |
| 1.0 | Initial artifact retained unchanged. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

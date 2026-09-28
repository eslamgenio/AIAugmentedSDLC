# E01 - Business Context

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.0

**Status:** Draft supporting input, based on requirements.md version 1.0.

Source: [requirements.md](../Requirements/requirements.md), feature version 1.0.

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

The objective is correct state/notification behavior, not a response-time or delivery-channel commitment. Use only the event ordering and functional scope defined in requirements.md. No interviews, user research, cost savings or production telemetry are claimed.

No unresolved behavior questions have been identified within the stated scope. Owner agreement is pending in E09.

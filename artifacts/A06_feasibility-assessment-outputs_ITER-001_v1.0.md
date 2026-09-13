# A06 - Feasibility Assessment Outputs

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.0

**Status:** Draft supporting input, based on requirements.md version 1.0.

Source: [requirements.md](requirements.md), feature version 1.0.

## A06-01 - Feasibility assessment and option comparison

Assessment: test design is feasible from the stated event/state rules. Use a controlled event simulator or equivalent test environment that can reset devices and expose status and notification records. No actual environment has been implemented or verified.

A physical-device/network test would introduce timing and transport concerns outside this feature; it is not needed for the current test-design scope. Cost and schedule have not been estimated.

## A06-02 - Risk register with mitigations and owners

Owner roles below are proposed; individuals have not been assigned.

| Risk | Impact | Test-design mitigation | Source links | Owner |
| --- | --- | --- | --- | --- |
| RISK-001 | Off-by-one detection marks a device offline too early or late. | Exercise below, at and above the three-miss threshold. | REQ-001; AC-001 to AC-003 | QA owner (unassigned) |
| RISK-002 | Misses before a received heartbeat remain in the count. | Interrupt misses with a valid heartbeat and verify a fresh sequence. | REQ-002; AC-004, AC-006, AC-007 | QA owner (unassigned) |
| RISK-003 | Continuing misses produce repeated alerts, or a later incident produces none. | Check notification count across continued misses, recovery and a new incident. | REQ-003; AC-008 to AC-011 | QA owner (unassigned) |
| RISK-004 | Events or alert suppression leak between devices. | Interleave events for at least two devices with different states. | REQ-004; AC-012, AC-013 | QA owner (unassigned) |

## A06-03 - Prototype or investigation recommendations

Before executing tests, verify that event injection, device reset, state observation and notification inspection are available. Direct observation of the counter is optional; reset behavior can also be checked through subsequent state transitions. This capability check is pending and does not block drafting test cases.

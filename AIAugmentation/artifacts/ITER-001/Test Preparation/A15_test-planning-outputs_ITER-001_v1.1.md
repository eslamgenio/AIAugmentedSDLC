# A15 - Test Planning Outputs

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.1

**Status:** Draft supporting input, based on the embedded A05-02 baseline version 1.0.

Source: [A05-02 baseline](../Requirements/A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02--proposed-baseline-with-revision-history), feature version 1.0.

## A15-01 - Test strategy and scoped test plan

Plan ID: DEVICE-CONNECTION-TEST-PLAN. Version: 1.0.

Objective: design functional tests for all four requirements and thirteen acceptance criteria in baseline DEVICE-CONNECTION-BASELINE v1.0.

Cover initial ONLINE state, the three-miss boundary, reset before the threshold, recovery, repeated incidents, one notification per incident, absence of offline notifications on received heartbeats, and interleaved device events. Prioritize risks RISK-001 through RISK-004 in A06. No fixed number of cases is required.

Excluded: registration, unknown devices, malformed/duplicate events, heartbeat scheduling, network transport, notification channels/retries, authentication, persistence and performance. These exclusions match the embedded A05-02 baseline.

## A15-02 - Test levels, responsibilities and schedule

- Level: component-level functional/state-transition test design using the logical interface in A09.
- Creator: create-test-cases produces A16; reviewer: review-test-coverage produces A17; QA owner provides the final human decision; an individual has not been assigned.
- Sequence: draft cases, review coverage, revise if findings warrant it, then re-review. No calendar deadline is supplied.
- Environment needs: reset registered devices, submit ordered event sequences, inspect statuses and notifications. Execution is not part of this exercise.

## A15-03 - Entry, exit and suspension criteria

Entry for drafting: requirements v1.0 and the supporting inputs are available. Formal baseline approval is pending in E09; draft test design may proceed without claiming approval.

Test-design exit: every criterion is accounted for; expected results follow the source; no unresolved blocking questions or blocking review findings remain; the reviewer identifies the candidate version. READY remains a recommendation, not execution success or actual human approval.

Suspend affected design decisions for a source conflict or missing expected behavior; continue unaffected work. A changed requirement requires affected cases and coverage to be rechecked.

## Revision history

| Artifact version | Change |
| --- | --- |
| 1.0 | Initial artifact retained unchanged. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

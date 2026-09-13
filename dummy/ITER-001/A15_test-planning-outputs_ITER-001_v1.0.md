# A15 — Test Planning Outputs

- **artifact_id:** A15
- **artifact_name:** Test Planning Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** plan-testing
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; event/state behavior only
- **Output filename:** `A15_test-planning-outputs_ITER-001_v1.0.md`

## Source references

[requirements.md](requirements.md), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.0.

## Required content

| Field | Value / section reference |
| --- | --- |
| `plan_id` | DEVICE-CONNECTION-TEST-PLAN v1.0 |
| `scope` | REQ-001–004 / AC-001–013; exclusions in requirements.md |
| `levels` | Component functional and state-transition design |
| `risks` | A06 v1.0, RISK-001–004 |
| `responsibilities` | A15-02; creator, reviewer and unassigned QA owner |
| `schedule` | Draft → review → revise → re-review; no calendar commitment |
| `entry_exit_suspension_criteria` | A15-03 |

## A15-01 — Test strategy and scoped test plan

Plan ID: DEVICE-CONNECTION-TEST-PLAN. Version: 1.0.

Objective: design functional tests for all four requirements and thirteen acceptance criteria in baseline DEVICE-CONNECTION-BASELINE v1.0.

Cover initial ONLINE state, the three-miss boundary, reset before the threshold, recovery, repeated incidents, one notification per incident, absence of offline notifications on received heartbeats, and interleaved device events. Prioritize risks RISK-001 through RISK-004 in A06. No fixed number of cases is required.

Excluded: registration, unknown devices, malformed/duplicate events, heartbeat scheduling, network transport, notification channels/retries, authentication, persistence and performance. These exclusions match requirements.md.

## A15-02 — Test levels, responsibilities and schedule

- Level: component-level functional/state-transition test design using the logical interface in A09.
- Creator: create-test-cases produces A16; reviewer: review-test-coverage produces A17; QA owner provides the final human decision; an individual has not been assigned.
- Sequence: draft cases, review coverage, revise if findings warrant it, then re-review. No calendar deadline is supplied.
- Environment needs: reset registered devices, submit ordered event sequences, inspect statuses and notifications. Execution is not part of this exercise.

## A15-03 — Entry, exit and suspension criteria

Entry for drafting: requirements v1.0 and the supporting inputs are available. Formal baseline approval is pending in E09; draft test design may proceed without claiming approval.

Test-design exit: every criterion is accounted for; expected results follow the source; no unresolved blocking questions or blocking review findings remain; the reviewer identifies the candidate version. READY remains a recommendation, not execution success or actual human approval.

Suspend affected design decisions for a source conflict or missing expected behavior; continue unaffected work. A changed requirement requires affected cases and coverage to be rechecked.

## Acceptance and handoff

Draft input for test design/review. Scope and source versions are explicit. Human agreement remains PENDING in E09; no approval gate is satisfied. Environment readiness is unverified and execution is outside scope. Correct any newly identified source conflict before relying on the affected behavior.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

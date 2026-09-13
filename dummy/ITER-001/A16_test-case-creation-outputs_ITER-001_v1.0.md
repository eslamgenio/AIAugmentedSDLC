# A16 — Test Case Creation Outputs

- **artifact_id:** A16
- **artifact_name:** Test Case Creation Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** create-test-cases
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; event/state behavior only
- **Output filename:** `A16_test-case-creation-outputs_ITER-001_v1.0.md`

## Source references

[requirements.md](requirements.md), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.0.

## A16-01 — Requirement-linked test cases and scenarios

Each case starts independently. Reset DEVICE-A to ONLINE, consecutive misses zero, and an empty notification log. M means HEARTBEAT_MISSED; H means HEARTBEAT_RECEIVED. Submit events once in order and inspect status and the complete notification log after each step. These are design expectations, not executed results.

### TC-001 — Threshold and continuing misses

- **req_ids:** REQ-001, REQ-003
- **ac_ids:** AC-001, AC-002, AC-003, AC-008, AC-009, AC-011
- **suite_type:** functional
- **Test type:** State transition / boundary
- **Status:** READY FOR REVIEW
- **preconditions:** Independent reset described above; event injection and observation assumed available for design.
- **data:** DEVICE-A and the ordered M/H events below.
- **Question references:** None.

| Step | Action | Observable expected result and source |
| --- | --- | --- |
| 1 | Inspect initialized DEVICE-A before sending events. | ONLINE; no notifications (AC-001, AC-011). |
| 2 | Send M to DEVICE-A once, then a second time; inspect after each event. | ONLINE after each event; no notifications (AC-001). |
| 3 | Send the third M to DEVICE-A. | OFFLINE; exactly one notification identifying DEVICE-A (AC-002, AC-008). |
| 4 | Send fourth and fifth M events; inspect after each. | OFFLINE; total remains one notification for DEVICE-A (AC-003, AC-009). |

**expected:** See TC-001 step 4 for the final outcome.

### TC-002 — Interrupt a miss sequence while online

- **req_ids:** REQ-001, REQ-002, REQ-003
- **ac_ids:** AC-001, AC-002, AC-004, AC-007, AC-008, AC-011
- **suite_type:** functional
- **Test type:** State transition / boundary
- **Status:** READY FOR REVIEW
- **preconditions:** Independent reset described above; event injection and observation assumed available for design.
- **data:** DEVICE-A and the ordered M/H events below.
- **Question references:** None.

| Step | Action | Observable expected result and source |
| --- | --- | --- |
| 1 | Send H to initialized DEVICE-A. | ONLINE; no notifications (AC-007, AC-011). |
| 2 | Send M, M, H to DEVICE-A; inspect after each. | ONLINE throughout; no notifications; H resets the miss sequence (AC-001, AC-004, AC-007, AC-011). |
| 3 | Send M, M; inspect after each. | ONLINE and no notifications after both events, demonstrating prior misses were cleared (AC-004). |
| 4 | Send one more M. | OFFLINE; exactly one notification for DEVICE-A (AC-002, AC-008). |

**expected:** See TC-002 step 4 for the final outcome.

### TC-003 — Recover and begin another incident

- **req_ids:** REQ-001, REQ-002, REQ-003
- **ac_ids:** AC-005, AC-006, AC-008, AC-009, AC-010, AC-011
- **suite_type:** functional
- **Test type:** State transition / boundary
- **Status:** READY FOR REVIEW
- **preconditions:** Independent reset described above; event injection and observation assumed available for design.
- **data:** DEVICE-A and the ordered M/H events below.
- **Question references:** None.

| Step | Action | Observable expected result and source |
| --- | --- | --- |
| 1 | Send M, M, M to DEVICE-A. | ONLINE after first and second; OFFLINE after third; one notification for DEVICE-A (AC-008). |
| 2 | Send H to DEVICE-A. | Immediately ONLINE; total notifications remains one (AC-005, AC-011). |
| 3 | Send M, M; inspect after each. | ONLINE; total notifications remains one (AC-006). |
| 4 | Send a third M. | OFFLINE; total notifications becomes two, both identifying DEVICE-A (AC-006, AC-010). |
| 5 | Send one more M. | OFFLINE; total remains two notifications (AC-009). |

**expected:** See TC-003 step 5 for the final outcome.

## A16-02 — Preconditions, data needs and expected results

| Test ID | Setup / environment capabilities | Data / fixtures | Expected result reference |
| --- | --- | --- | --- |
| TC-001 | Reset, ordered event injection, status and notification inspection | DEVICE-A; case-specific event sequence | TC-001 numbered steps in A16-01 |
| TC-002 | Reset, ordered event injection, status and notification inspection | DEVICE-A; case-specific event sequence | TC-002 numbered steps in A16-01 |
| TC-003 | Reset, ordered event injection, status and notification inspection | DEVICE-A; case-specific event sequence | TC-003 numbered steps in A16-01 |

## A16-03 — Coverage questions and automation candidates

### Questions

None identified within the source scope.

### Automation candidates

TC-001, TC-002 and TC-003: repeatable event sequences with observable status and notification assertions. Requires a controllable component harness; none is supplied or verified.

### Scope accounting

REQ-001–003 / AC-001–011 are addressed by TC-001–003. REQ-004 / AC-012–013 have no cases in this candidate.

### Responses to prior review findings

Not applicable — initial draft.

## Acceptance and handoff

Case IDs are unique and expected results are specified. This candidate is incomplete and ready for independent review, not acceptance. No tests have been executed. Pass this exact v1.0 candidate and source inputs to review-test-coverage.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial candidate. |

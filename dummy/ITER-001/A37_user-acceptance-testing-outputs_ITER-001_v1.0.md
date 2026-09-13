# A37 — User Acceptance Testing Outputs

- **artifact_id:** A37
- **artifact_name:** User Acceptance Testing Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** support-uat
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A37_user-acceptance-testing-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A04 — Acceptance Criteria Outputs](A04_acceptance-criteria-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A16 — Test Case Creation Outputs](A16_test-case-creation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A33 — Test Exit Assessment Outputs](A33_test-exit-assessment-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E09 — Human Decisions](E09_human-decisions_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `scenario_ids` | UAT-001: operator observes loss, recovery and another incident |
| `candidate_id` | RC-002 / B002 |
| `participants` | Product owner and IoT operations representative; unassigned |
| `guidance` | Observe device identity, status and incident count using the case narrative |
| `user_results` | NOT RUN; no participant session supplied |
| `issues` | UAT-ISSUE-001: participants and acceptance evidence missing |
| `acceptance_refs` | None |
| `pending_decisions` | Business acceptance and test exit PENDING |

## A37-01 — UAT scenario pack and participant guidance

UAT-001 follows DEVICE-A through loss, recovery and a new incident; compare observations with AC-005/008/010.

## A37-02 — User results, feedback and issue log

No user results or feedback session has occurred. Do not reuse engineering case results as user acceptance.

## A37-03 — Acceptance evidence and pending business decisions

Schedule participants after exit blockers are addressed and record their actual candidate-specific decision.

## Acceptance and handoff

**Acceptance checks:** User outcomes are attributable. Business acceptance is recorded only when actually supplied.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H113, H116

**If incomplete:** Return invalid or incomplete output to support-uat. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

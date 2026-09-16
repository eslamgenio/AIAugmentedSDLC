# E06 — Test and Defect Baselines

- **artifact_id:** E06
- **artifact_name:** Test and Defect Baselines
- **iteration_id:** ITER-001
- **artifact_version:** 1.1
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** Test lead and defect system
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** the embedded A05-02 baseline v1.0; event/state behavior only
- **Output filename:** `E06_test-and-defect-baselines_ITER-001_v1.1.md`

## Source references

[A05-02 baseline](A05_requirements-review-outputs_ITER-001_v1.1.md#a05-02-proposed-baseline-with-revision-history), feature version 1.0. Supporting inputs in this folder share iteration ITER-001 and artifact version 1.1.

## Required content

| Field | Value / section reference |
| --- | --- |
| `baseline_id` | DEVICE-CONNECTION-TEST-ASSETS v1.0 |
| `suite_type` | Functional component/state-transition |
| `case_template` | ../../templates/A16_test-case-creation-outputs.md |
| `coverage_rules` | See Coverage and review rules |
| `workload` | Not applicable; performance excluded |
| `defect_ids` | Not supplied; no conclusion that register is empty |
| `taxonomy` | Expectation, coverage, clarity, duplicate, traceability; BLOCKING/NONBLOCKING |
| `snapshot_time` | 2026-09-13 snapshot |

## Test baseline

Baseline ID: DEVICE-CONNECTION-TEST-ASSETS. Version: 1.0. Owner: Test lead (unassigned).
Suite type: functional component/state-transition test design.

## Test-case template

Each case should contain:

- Stable test ID and descriptive title.
- Requirement IDs and acceptance-criterion IDs.
- Test type, such as functional, negative or boundary.
- Preconditions and concrete event/device data.
- Numbered steps with observable expected results, including intermediate checkpoints where relevant.
- Design status: READY FOR REVIEW or BLOCKED, with linked question IDs when blocked.

Use a readable Markdown A16 bundle with its three catalog child sections. Keep setup and expected-result summaries consistent with the detailed cases. This document is a template, not a generated test suite.

## Coverage and review rules

- Account for all AC-001 through AC-013 and all four requirements. Criterion links alone do not prove coverage.
- Exercise zero, one, two, three and more than three consecutive misses where relevant to the threshold and notification behavior.
- Include interrupted sequences, recovery followed by a new incident, and independent/interleaved device events.
- Accept equivalent representative data where behavior is the same; preserve exact values where the three-miss boundary matters.
- Check notification identity and count, not only device status. Do not add excluded error or performance behavior as mandatory coverage.
- Avoid redundant cases, guessed outcomes and unresolved blocking questions. Preserve test IDs across revisions.

## Existing suites, workloads and defects

Existing suite baseline: not supplied; this input supports a new design. Existing defect register: not supplied. No conclusion about existing defects is made.

Workload/performance targets: not applicable to this scope. Use devices DEVICE-A and DEVICE-B as illustrative identifiers; they are not real assets. If review findings arise, classify them as expectation, coverage, clarity, duplicate or traceability issues, with BLOCKING/NONBLOCKING severity.

## Acceptance and handoff

Draft input for test design/review. Scope and source versions are explicit. Human agreement remains PENDING in E09; no approval gate is satisfied. Environment readiness is unverified and execution is outside scope. Correct any newly identified source conflict before relying on the affected behavior.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |
| 1.1 | Updated baseline references to self-contained A05 v1.1; content, IDs and pending decisions preserved. |

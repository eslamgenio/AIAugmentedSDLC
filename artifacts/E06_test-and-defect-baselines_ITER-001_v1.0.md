# E06 - Test and Defect Baselines

Feature: DEVICE-CONNECTION | Iteration: ITER-001 | Artifact version: 1.0

**Status:** Draft supporting input, based on requirements.md version 1.0.

Source: [requirements.md](requirements.md), feature version 1.0.

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

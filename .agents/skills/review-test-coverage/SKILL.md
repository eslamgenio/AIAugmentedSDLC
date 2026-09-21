---
name: review-test-coverage
description: Review software test cases against requirements and acceptance criteria for coverage, correct expectations, clarity, and duplicates. Produces the A17 traceability and actionable review bundle, including verification of prior corrections. Use to review test design, not to report test execution results.
---

# Review test coverage

Independently assess whether the supplied cases adequately test the specified feature. Review content and observable behavior, not merely the presence of requirement links. Use the supplied requirements and test cases directly; no custom runner or creator skill is required.

## Establish the review basis

- Read the requirements and acceptance criteria, the candidate test cases, and any supplied risks, domain rules, scope or template. Accept an A16 bundle or an existing test document in another format.
- Record the exact candidate filename/version and the source requirements used. If no version exists, identify the supplied document or pasted snapshot; do not invent a verified version or checksum.
- If requirements or candidate tests are missing, ask for them. Missing optional supporting documents should be noted as limitations rather than automatically blocking a useful review.
- Preserve source IDs. If absent, assign local labels and map them to original source text. Do not add requirements silently.
- A creator's coverage claims or previous READY decision are evidence to inspect, not conclusions to adopt. Use the current candidate; never apply a prior review to a changed document without rechecking it.

### Named input artifacts

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the requirements baseline from A05 and its embedded content or referenced baseline, together with A04 acceptance criteria. Also accept supplied requirements documents or text regardless of filename; no particular requirements filename is mandatory. If A05 embeds the complete behavior, context and scope, a separate requirements file is unnecessary. Follow an external baseline reference when needed to obtain missing content; ask only when essential behavior or scope is still missing or conflicting. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft or review under the rules above.

- `A16_test-case-creation-outputs_{iteration_id}_v{artifact_version}.md`
- `A05_requirements-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A04_acceptance-criteria-outputs_{iteration_id}_v{artifact_version}.md`
- `A06_feasibility-assessment-outputs_{iteration_id}_v{artifact_version}.md`
- `E06_test-and-defect-baselines_{iteration_id}_v{artifact_version}.md`

For re-review, also read the prior `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md` when present, alongside the revised A16 candidate and its creator responses.

## Review the content

1. For each requirement/criterion, identify the behaviors and meaningful scenarios that need testing. Compare these with actual case steps, data and expected results. Distinguish full coverage, partial coverage, no coverage and behavior blocked by ambiguous requirements.
2. Re-derive expected results from the supplied rules. Check boundaries, validation, roles, state changes and failure behavior where relevant. Flag invented expectations and claims that lack a source. A test ID linked to a criterion does not by itself demonstrate coverage.
3. Accept representative alternatives within the same input category. For example, two different fractional values can both test integer-only validation. Require precise boundary values when the requirement makes them significant; do not demand an arbitrary example value as the only valid test.
4. Check that the tester can understand the setup, obtain the data, perform the steps and observe the expected result. Identify contradictions, missing preconditions and duplicated behavior. Similar wording alone is not a duplicate when roles, states or outcomes differ.
5. Report each substantive issue with a stable finding ID, affected requirement/test IDs, exact location or short evidence excerpt, why it matters, and a concrete requested correction. For a missing test, point to the uncovered source statement; do not invent a test ID that does not exist.
6. Separate creator-fixable defects from questions requiring a business decision. Suggest a correction when supported; do not choose unspecified behavior on the owner's behalf.

## Output: A17 — Test Coverage Review Outputs

When working in this project, read and follow the [A17 template](../../../AIAugmentation/templates/A17_test-coverage-review-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. A user-supplied format takes precedence.

Use the user's requested format and location. Otherwise write one readable Markdown document in the active `AIAugmentation/artifacts/<iteration_id>/` folder, named `A17_test-coverage-review-outputs_{iteration_id}_v1.0.md` for a first standalone review. Substitute the candidate's iteration ID; if none is available, start with `ITER-001`. Reuse the candidate's iteration convention, increment review versions, and preserve previous reviews. If file writing is unavailable, return the same content in the conversation.

Start with the feature, A17 version, exact candidate reference, requirements sources, scope and overall recommendation. Use these stable sections:

- **A17-01 — Requirements-to-tests traceability matrix:** one row per acceptance criterion, or per requirement when criteria are not supplied. Include source ID, linked test IDs, FULL / PARTIAL / NONE / BLOCKED coverage and a brief explanation. A requirement is fully covered only if its applicable criteria are fully covered. Use NOT APPLICABLE only with an explicit scope justification.
- **A17-02 — Coverage gap and duplicate case report:** missing scenarios and duplicate groups, linked to findings. Explain why a duplicate adds no distinct coverage. State explicitly if there are none.
- **A17-03 — Test review findings and revision actions:** findings with ID, severity (BLOCKING or NONBLOCKING), evidence, requested action and disposition. BLOCKING means the design should not be accepted as-is; NONBLOCKING is an improvement that does not undermine adequacy. Include the verification result for each prior finding when reviewing a revision.

Choose one recommendation:

- **READY:** adequate coverage in the stated scope, no blocking design defects or unresolved questions affecting expected behavior. Disclose remaining nonblocking suggestions and any review limitations.
- **REVISE:** the creator can address material issues using the existing requirements. List actionable corrections.
- **BLOCKED:** an essential ambiguity, conflict or missing input requires an owner decision. State the specific question; still report other review findings.

READY is a test-design recommendation, not human approval or evidence that application tests passed. This is a human-readable A17 document profile. If machine-readable output is requested, use the agreed schema and check compatibility before claiming it.

## Re-review and handoff

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

When a revised candidate is supplied, read the prior findings and creator responses. Check the actual changed cases, verify every previous finding, and check for regressions introduced by the changes. Preserve finding IDs; mark them resolved only when evidence supports closure. Retain unresolved IDs and use new IDs for newly discovered issues.

Finish with a link to A17, the recommendation and the most important next action. The creator can consume A17 alongside the reviewed A16 and the same requirements. Do not silently rewrite A16 during review, start a correction loop, execute tests or publish results externally unless the user requested that work.

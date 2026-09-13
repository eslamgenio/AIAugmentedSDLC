---
name: create-test-cases
description: Create or revise requirement-linked software test cases with preconditions, data, expected results, and open questions. Use for test design from requirements or acceptance criteria, including corrections requested by a coverage review. Produces the A16 test-design bundle; does not execute tests.
---

# Create test cases

Turn the user's requirements into test cases another tester can carry out. Work across domains; choose steps, data and coverage appropriate to the supplied feature. Use the supplied requirements directly; no custom runner or other skill is required.

## Inputs and scope

- Read the supplied requirements and acceptance criteria, plus any relevant design details, risks, domain rules or test template. Files, pasted text and existing project documents are acceptable. Preserve source IDs and versions where provided.
- For revisions, also read the prior test cases and the review findings or user feedback.
- If the feature requirements are absent, ask for them. Otherwise start with the usable information. Missing formal approval, risk documents or a template does not prevent a clearly marked draft.
- Do not invent behavior, interface details, limits, messages or error codes. Record a targeted question when missing information changes the expected result; continue unaffected cases. Distinguish user requirements from suggested additional checks.
- If source statements lack IDs, assign local REQ/AC labels and show the source-text mapping. These labels organize existing statements; they do not create new acceptance criteria.

## Design the cases

1. Identify observable behavior, applicable constraints and the conditions that change an outcome. Cover normal flows, meaningful negative cases and boundaries. Include roles, states, transitions or integrations when relevant to the supplied feature; avoid an unrelated test-category checklist.
2. Select representative values for equivalent input categories. Use precise below/at/above values for specified boundaries. A particular example value is mandatory only when required by the source or agreed coverage rules.
3. Give each case a stable test ID, title, requirement/criterion links, test type, preconditions, concrete data, numbered steps and observable expected results. State expected intermediate results when they matter. Derive expectations from the source, not from assumptions or existing implementation behavior alone.
4. Mark scenarios with unresolved expectations as BLOCKED and link their question IDs. Use READY FOR REVIEW for specified cases; neither status means execution passed. Do not write a guessed result as a fact.
5. Keep cases distinct and sufficient. Split scenarios whose outcomes or setup differ; avoid multiplying identical behavior solely to increase the case count.
6. Identify automation candidates with a short reason based on repeatability, observable results and setup. This is a suggestion, not a claim that automation exists.

Before delivery, check that IDs are unique, references resolve, steps are executable as written, expectations follow the source, and every requirement/criterion is covered or explicitly listed as blocked, out of scope or needing clarification. Explain any exclusions.

## Output: A16 — Test Case Creation Outputs

Use the user's requested format and location. Otherwise write one readable Markdown document in the project `artifacts/` folder, named `A16_test-case-creation-outputs_ITER-001_v1.0.md` for a first standalone draft. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Include a short header with the feature, A16 version, source filenames/versions or source-text mapping, scope and draft/review status. Then use these stable sections:

- **A16-01 — Requirement-linked test cases and scenarios:** the cases, with the fields above. Prefer per-case blocks if a wide table would hide steps or expectations.
- **A16-02 — Preconditions, data needs and expected results:** a compact setup/data summary by test ID. Reference the detailed expected results in A16-01 rather than maintain conflicting copies. Note required accounts, fixtures or environment capabilities only where relevant.
- **A16-03 — Coverage questions and automation candidates:** questions with ID, affected cases/requirements and blocking impact; list automation candidate test IDs with reasons. State explicitly when there are none.

This is a human-readable A16 document profile. If the user requests machine-readable output, use their agreed schema and check compatibility before claiming it.

## Revisions and handoff

Preserve IDs for the same logical cases. Assign new IDs to new cases; record removed or superseded cases without reusing their IDs. Include a short response for each review finding: changed, retained with explanation, or blocked pending clarification. Cite the affected test IDs. Do not mark review findings independently verified; the reviewer does that.

Finish with a link to A16 and a brief note about unresolved questions. It can be passed, together with the same source requirements, to `review-test-coverage`. Invoke that skill only when the user's scope includes review. Do not automatically repeat creation/review, execute tests or publish to a test-management system.

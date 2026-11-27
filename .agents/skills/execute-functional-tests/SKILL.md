---
name: execute-functional-tests
description: DSK Execute or record system and functional test cases against an identified build and environment, with actual results, requirement-linked evidence, failure details, blocked-test reasons and defect candidates. Produces the A29 functional-testing bundle; runs only the authorized cases and does not design cases, deploy, fix or triage defects, or approve test exit.
---

# Execute functional tests

Run the designed functional cases, or record a supplied run, so that every executed case has an actual result next to its expected result and its requirement links. Work across domains and interfaces, whether the cases are manual, automated or mixed. No custom runner or other skill is required; use the project's own tools.

## Optional project guide

Before executing functional tests, look for `AIAugmentation/project_guides/execute-functional-tests-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, environments, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-execution boundaries.

## Inputs and scope

- Read the designed cases (A16) and their coverage review (A17), the acceptance criteria (A04), the deployed build and environment (A26), and the prepared test resources and environment records (A18 and E07). Files, pasted text, supplied automation and existing project documents are acceptable. Preserve source IDs and versions where provided.
- If designed cases are absent, ask for them; test design belongs to `create-test-cases`. If expected results are missing or a case is BLOCKED in A16, do not supply a guessed expectation: mark the case BLOCKED with the linked question and continue with the rest.
- Treat a READY A17 recommendation and the A15 plan as context, not as proof that the cases are adequate or that execution may start. Record when A17 is REVISE or BLOCKED, or when an A15 entry criterion is not met, and still record what the user asked you to run.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the designed cases and expected results from A16, their review status from A17, the acceptance criteria from A04, and the build and environment identity from A26 and E07. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A16_test-case-creation-outputs_{iteration_id}_v{artifact_version}.md`
- `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A04_acceptance-criteria-outputs_{iteration_id}_v{artifact_version}.md`
- `A26_test-deployment-outputs_{iteration_id}_v{artifact_version}.md`
- `A18_test-resources-outputs_{iteration_id}_v{artifact_version}.md`
- `E07_environment-and-access-records_{iteration_id}_v{artifact_version}.md`
- `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`

For revisions or re-runs, also read the supplied prior `A29_functional-testing-outputs_{iteration_id}_v{artifact_version}.md` and the changed build or case revisions that prompted the re-run.

## Authorization and execution boundary

- Run tests only when the user's request includes execution for the named build and environment. Otherwise, or when the environment cannot be reached, record results from supplied execution evidence, or plan the run and mark each case NOT RUN with the reason. Never present planned, designed or expected results as executed results.
- Use only the build, environment, accounts, data and commands identified by the user, the project instructions (for example their required checks or commands), the optional guide, A18 test resources or E07 environment records. Do not guess a command, endpoint or credential. If the identified command or environment is missing, ask for it and continue with work that does not depend on it.
- Stay within the test activity. Do not deploy or rebuild the application, change application code, test assets or environment configuration, close or file defects in an external tracker, or publish results externally. Do not run against production or with real personal data, secrets or shared resources unless the user explicitly authorizes that target and the project rules allow it; report the gap instead of working around it.
- Record what actually ran: the command or procedure, the start and end time when available, the tool and version, and the exact native output location. Redact secrets and personal data from copied evidence and link the native file instead of pasting large output.

## Run the tests

1. **Pin the basis.** Record the exact `build_id` (with its digest or source revision when available), `env_id`, and the A16, A17 and A04 revisions used. Confirm that the deployed build in A26 matches the build under test; if it cannot be confirmed, record the mismatch as a limitation and do not merge results across builds.
2. **Select the cases.** List the case IDs in scope with their requirement and criterion IDs. Run cases as designed; do not add, merge or reword cases. List every in-scope criterion without a designed case as a coverage gap linked to A17, not as a passed, blocked or not-run result.
3. **Check readiness.** Confirm that the setup, data, accounts and environment capabilities each case needs are available. When a prerequisite is missing, mark the affected cases BLOCKED with the obstacle and run the rest.
4. **Execute or record.** Run the authorized cases with the identified procedure or automation, or import the supplied run. For each case record the actual result at each step or checkpoint that has an expected result, not only the final outcome.
5. **Classify results.** Give every in-scope case exactly one status. For a FAILED case, record the first failing step or checkpoint, the expected and actual values, and the affected requirement and criterion. Distinguish a product failure from an environment or test-data failure; the latter makes the case BLOCKED, not FAILED, unless the evidence shows otherwise.
6. **Raise defect candidates.** Link each candidate to the failing case and its evidence.

Use these execution statuses for every in-scope case, and define them in the artifact:

- **PASSED:** executed, and every checked result matched the expected result in the designed case.
- **FAILED:** executed, and at least one actual result differed from the expected result in the designed case. Record the first failing step or checkpoint, the expected value and the actual value.
- **BLOCKED:** execution was attempted or due but could not complete because of a named obstacle, such as an unavailable environment, dependency, data, access or an unresolved question. Link the obstacle.
- **NOT RUN:** not attempted in this run, with the reason (for example out of the selected scope, not authorized or no designed case).

Only PASSED and FAILED count as executed. Keep BLOCKED and NOT RUN separate from executed results and from each other. A criterion without a designed case is a coverage gap, not a BLOCKED or NOT RUN result.

For each FAILED case, raise a defect candidate with a stable ID (for example `DC-###`, or the existing defect ID when the defect is already registered in E06 or A34), the case ID, affected requirement and criterion IDs, build and environment, expected and actual results, reproduction steps and the evidence path. Propose a severity only when the project's defect taxonomy supplies one, and mark it as proposed. Triage, priority and assignment belong to `triage-defects` (A34); do not file the candidate in a defect tracker.

Before delivery, check that every executed case has actual results and evidence, BLOCKED and NOT RUN cases remain separate with reasons, coverage gaps are not counted as results, every result names its build and environment, and no actual result was inferred from an expected one.

## Output: A29 — Functional Testing Outputs

When working in this project, read and follow the [A29 template](../../../AIAugmentation/templates/A29_functional-testing-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A29_functional-testing-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Execution/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep native evidence in its original format and link it.

Include a short header with the feature, A29 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `test_ids`, `req_ids`, `ac_ids`, `build_id`, `env_id`, `actual`, `expected`, `status` and `evidence`, referencing the child sections or native evidence rather than duplicating them. Then use these stable sections:

- **A29-01 — Test execution records with actual results:** One record per case with build, environment, executor or tool, date, status and the actual result at each step or checkpoint that has an expected result, followed by status counts for the run.
- **A29-02 — Requirement-linked evidence and failure details:** Per requirement and criterion, the linked cases and their statuses with evidence paths, and for each failure the failing step or checkpoint with expected and actual values. List uncovered criteria separately as coverage gaps.
- **A29-03 — Defect candidates and blocked-test reasons:** The defect candidates and, for every BLOCKED or NOT RUN case, the reason and what would unblock it. State explicitly when there are none.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native evidence files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A29-01 through A29-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` is not test-exit approval, and passing cases are not acceptance of the requirements. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Preserve case IDs and defect candidate IDs. A re-run on another build is a new artifact version that keeps the earlier results visible; never overwrite a FAILED result with a later PASSED one. For each prior defect candidate, state whether the re-run reproduced it, no longer reproduced it, or did not exercise it. Retesting a fixed defect belongs to `retest-defects` (A36) when that skill is used.

Finish with a link to A29, the status counts, the defect candidates and the coverage gaps. A29 can be passed to `triage-defects` (A34) for failures, and to `report-test-progress` (A32) and `assess-test-readiness` (A33). Invoke those skills only when the user's scope includes that work. Do not automatically triage or fix defects, re-run tests on a new build, declare test exit or publish results externally.

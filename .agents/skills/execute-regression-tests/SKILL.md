---
name: execute-regression-tests
description: DSK Select and execute, or record, a regression suite traced to the changes in an identified build, with the selection rationale, results and evidence, new failures, excluded coverage and residual risks. Produces the A31 regression-testing bundle; runs only the authorized tests and does not fix or triage defects, or approve test exit.
---

# Execute regression tests

Choose the existing tests that the changes in a build could affect, run them, or record a supplied run, and make clear what was deliberately left out. Selection must trace to the changes and to coverage, not to convenience. Work across domains and tools; no custom runner or other skill is required.

## Optional project guide

Before selecting or executing regression tests, look for `AIAugmentation/project_guides/execute-regression-tests-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, regression suites, environments, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-execution boundaries.

## Inputs and scope

- Read the designed cases and their coverage review (A16 and A17), the automation and regression baselines (A19 and E06), the changes under test (A20 implementation, A22 review and A35 defect fixes), and the build, environment and resources (A26, E07 and A18). Files, pasted text, change lists and existing project documents are acceptable. Preserve source IDs and versions where provided.
- If the changes in the build cannot be identified, ask for them. Without a change list, select only with the user's agreement (for example the full suite) and record that the selection does not trace to changes.
- Regression selection uses existing designed tests. Note missing tests for changed behavior as coverage gaps; test design belongs to `create-test-cases`.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the candidate tests from A16, A17, A19 and E06, the changes from A20, A22 and A35, and the build and environment identity from A26 and E07. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A16_test-case-creation-outputs_{iteration_id}_v{artifact_version}.md`
- `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A19_test-automation-outputs_{iteration_id}_v{artifact_version}.md`
- `E06_test-and-defect-baselines_{iteration_id}_v{artifact_version}.md`
- `A20_feature-implementation-outputs_{iteration_id}_v{artifact_version}.md`
- `A22_code-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A35_defect-fix-outputs_{iteration_id}_v{artifact_version}.md`
- `A18_test-resources-outputs_{iteration_id}_v{artifact_version}.md`
- `A26_test-deployment-outputs_{iteration_id}_v{artifact_version}.md`
- `E07_environment-and-access-records_{iteration_id}_v{artifact_version}.md`

For revisions or re-runs, also read the supplied prior `A31_regression-testing-outputs_{iteration_id}_v{artifact_version}.md` and the new build or changes that prompted the re-run.

## Authorization and execution boundary

- Run tests only when the user's request includes execution for the named build and environment. Otherwise, or when the environment cannot be reached, record results from supplied execution evidence, or plan the run and mark each case NOT RUN with the reason. Never present planned, designed or expected results as executed results.
- Use only the build, environment, accounts, data and commands identified by the user, the project instructions (for example their required checks or commands), the optional guide, A18 test resources, A19 automation or E07 environment records. Do not guess a command, endpoint or credential. If the identified command or environment is missing, ask for it and continue with work that does not depend on it.
- Stay within the test activity. Do not deploy or rebuild the application, change application code, test assets or environment configuration, close or file defects in an external tracker, or publish results externally. Do not run against production or with real personal data, secrets or shared resources unless the user explicitly authorizes that target and the project rules allow it; report the gap instead of working around it.
- Record what actually ran: the command or procedure, the start and end time when available, the tool and version, and the exact native output location. Redact secrets and personal data from copied evidence and link the native file instead of pasting large output.

## Run the tests

1. **Pin the basis.** Record the exact `build_id`, the baseline build it is compared with when known, `env_id`, and the change, review and fix revisions used. Give the suite a stable `suite_id` (reuse an existing one on re-run).
2. **Analyze impact.** List each change with the components, interfaces, requirements and risks it touches. Use supplied change records and code-review evidence; do not infer changes that are not evidenced.
3. **Select the suite.** For each selected test, record the change or risk that justifies it. Include retests of fixed defects only as regression checks of surrounding behavior; confirming the fix itself belongs to `retest-defects` (A36). List every excluded candidate test or area with its reason, and every affected area without a test as a coverage gap.
4. **Check readiness.** Confirm the build, environment, data and automation are available. When a prerequisite is missing, mark the affected tests BLOCKED with the obstacle and run the rest.
5. **Execute or record.** Run the authorized selection, or import the supplied run, and record actual results against expected results with evidence.
6. **Classify results.** Give every selected test exactly one status. Mark each FAILED test as a new failure, a known open defect or a previously passing test that now fails, using the prior results when supplied. Raise defect candidates for new failures.

Use these execution statuses for every in-scope test, and define them in the artifact:

- **PASSED:** executed, and every checked result matched the expected result in the designed case or automated check.
- **FAILED:** executed, and at least one actual result differed from the expected result in the designed case or automated check. Record the first failing step or checkpoint, the expected value and the actual value.
- **BLOCKED:** execution was attempted or due but could not complete because of a named obstacle, such as an unavailable environment, dependency, data, access or an unresolved question. Link the obstacle.
- **NOT RUN:** not attempted in this run, with the reason (for example out of the selected scope, not authorized or no designed case).

Only PASSED and FAILED count as executed. Keep BLOCKED and NOT RUN separate from executed results and from each other. A criterion without a designed test is a coverage gap, not a BLOCKED or NOT RUN result.

For each FAILED test, raise a defect candidate with a stable ID (for example `DC-###`, or the existing defect ID when the defect is already registered in E06 or A34), the test ID, affected requirement and criterion IDs, build and environment, expected and actual results, reproduction steps and the evidence path. Propose a severity only when the project's defect taxonomy supplies one, and mark it as proposed. Triage, priority and assignment belong to `triage-defects` (A34); do not file the candidate in a defect tracker.

Before delivery, check that every selected test traces to a change or risk, exclusions and coverage gaps are explicit, every executed test has actual results and evidence on the stated build, and residual risks from exclusions are stated.

## Output: A31 — Regression Testing Outputs

When working in this project, read and follow the [A31 template](../../../AIAugmentation/templates/A31_regression-testing-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A31_regression-testing-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Execution/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep native evidence in its original format and link it.

Include a short header with the feature, A31 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `suite_id`, `selected_test_ids`, `impact_rationale`, `build_id`, `results`, `exclusions` and `residual_risks`, referencing the child sections or native evidence rather than duplicating them. Then use these stable sections:

- **A31-01 — Selected regression scope and selection rationale:** The suite ID, the changes and their impact, the selected tests with the change or risk behind each, and the selection method.
- **A31-02 — Regression results with evidence and build ID:** One row per selected test with build, environment, status, actual result summary and evidence path, followed by status counts.
- **A31-03 — New failures, excluded coverage and residual risks:** New failures and their defect candidates, excluded tests and areas with reasons, coverage gaps, and the residual risk each exclusion or gap leaves. State explicitly when there are none.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native evidence files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A31-01 through A31-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` is not test-exit approval, and a passing regression selection does not show that unselected or uncovered behavior works. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Preserve the suite ID, test IDs and defect candidate IDs. A run on another build is a new artifact version that keeps the earlier results visible; never overwrite a FAILED result with a later PASSED one.

Finish with a link to A31, the status counts, new failures and residual risks. A31 can be passed to `triage-defects` (A34) for new failures, and to `report-test-progress` (A32) and `assess-test-readiness` (A33). Invoke those skills only when the user's scope includes that work. Do not automatically triage or fix defects, widen the suite, re-run on a new build, declare test exit or publish results externally.

---
name: build-test-automation
description: DSK Build or revise automated tests for selected designed test cases, with reusable fixtures, execution configuration, reporting integration, a setup guide and recorded framework validation against an identified code revision. Produces the A19 test-automation bundle consumed by smoke, integration and regression execution; does not change application code, run the formal test campaign, fix or triage defects, or approve test exit.
---

# Build test automation

Turn selected designed test cases into runnable automated checks that an execution skill, a CI job or another engineer can run without reinterpreting the cases, and record evidence that the automation itself works. Work across domains, languages and test frameworks; follow the project's existing test structure and tools. No custom runner or other skill is required.

## Optional project guide

Before building test automation, look for `AIAugmentation/project_guides/build-test-automation-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, frameworks, test directories, identifiers, commands, reporting formats and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-automation boundaries.

## Inputs and scope

- Read the designed cases and their automation candidates (A16, especially A16-03), the coverage review of those cases (A17), the components and interfaces under test (A09), the repository, framework and CI evidence (E05), and the prepared datasets, environment and setup (A18). Use the plan's levels and responsibilities (A15) as context when available. Files, pasted text, existing test code and project documents are acceptable. Preserve source IDs and versions where provided.
- Automate only designed cases. Select the A16 automation candidates, or the test IDs the user names, and record the reason for each selection or exclusion. If no designed case or selection can be identified, ask for it. A case whose expected result is open or ambiguous stays unautomated with the question recorded; test design belongs to `create-test-cases`.
- Treat a READY A17 recommendation as context, not proof that the cases are adequate. Record when A17 is REVISE or BLOCKED, or when an A17 finding affects a selected case, and still automate what the user asked for with that limitation visible.
- If the project's language, framework, test location or run command cannot be identified from the user, the project instructions, the optional guide or E05, ask for it. Do not introduce a new framework, dependency or CI pipeline without the user's agreement.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the selected cases and automation candidates from A16 and their review status from A17, the interfaces and components under test from A09, the repository revision, framework and CI conventions from E05, and the datasets, environment and setup from A18. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A16_test-case-creation-outputs_{iteration_id}_v{artifact_version}.md`
- `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A09_system-component-design-outputs_{iteration_id}_v{artifact_version}.md`
- `E05_repository-and-ci-evidence_{iteration_id}_v{artifact_version}.md`
- `A18_test-resources-outputs_{iteration_id}_v{artifact_version}.md`
- `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`

For revisions, also read the supplied prior `A19_test-automation-outputs_{iteration_id}_v{artifact_version}.md` and the changed cases, findings, code revision, flaky or failing validation evidence or feedback that prompted the revision.

## Authorization and automation boundary

- Write automated test code, fixtures and execution configuration in the project's existing test locations and conventions, identified by the user, the project instructions, the optional guide or E05. Do not modify application code, production configuration or unrelated tests. Do not overwrite or weaken existing tests; extend them or add new files, and record any existing test you had to change and why.
- Run validation only when the user's request includes it, using the command and environment identified by the user, the project instructions, the optional guide, A18 or E05. Do not guess a command, endpoint or credential. Otherwise mark each check NOT VALIDATED with the reason. Never present an unvalidated check as working.
- Validation shows that the automation runs and asserts correctly; it is not the formal test campaign. Product results observed during validation are recorded as validation evidence and handed to the execution skills rather than reported as execution results.
- Stay within the automation activity. Do not deploy or rebuild the application, change shared environments, commit, push, merge or alter CI pipelines, file defects in a tracker or publish results externally unless the user explicitly asks and the project rules allow it. Do not run against production or with real personal data, secrets or shared resources unless the user explicitly authorizes that target and the project rules allow it. Reference credentials by managed location or variable name, never by value.

## Build the automation

1. **Pin the basis.** Record the exact `code_revision` the automation targets (commit, tag, package digest or build ID), the A16, A17, A09, E05 and A18 revisions used, and the framework, language and tool versions.
2. **Select the cases.** List the `test_ids` to automate with their requirement and criterion links and the reason for each, and the candidates excluded with their reasons. Classify the `suite_type` of each, for example unit, component, API, integration, UI, smoke or regression, consistent with the A15 levels when supplied.
3. **Write the checks.** Implement each selected case so its steps and assertions match the designed preconditions, data, steps and expected results. Keep the A16 test ID in the test name, tag or metadata so results trace back. Assert observable outcomes, avoid fixed sleeps and order dependence, and keep each test independent and repeatable. Do not weaken an assertion to make a check pass, and do not encode current implementation behavior where it differs from the designed expected result.
4. **Build reusable fixtures.** Create fixtures, helpers, stubs and data loaders for shared setup and teardown, using the A18 datasets and setup by reference rather than copying or inventing data. Record which side of each interaction a stub replaces.
5. **Configure execution and reporting.** Provide the run `command`, the configuration files (`config_refs`) such as environment variables by name, tags or suites and timeouts, and the result format that execution and progress reporting can consume, for example JUnit XML or JSON with test ID, code revision, build, status, expected and actual values and timing. State the exit-code behavior.
6. **Validate the automation.** When authorized, run the checks against the identified revision and environment. Confirm that each check executes, that its assertions detect a failure (for example by a recorded known failure, a negative control or a deliberately broken input in a local copy), and that repeated runs give consistent results. Record the command, date, environment, tool versions, native result file path and checksum.
7. **Write the setup guide.** Give the prerequisites, installation steps, dataset and environment references from A18, the run command for each suite, how to read the results and known limitations, so another engineer can reproduce the validation.

Use these validation statuses for every automated check, and define them in the artifact:

- **VALIDATED:** the check ran on the recorded code revision and environment, its assertions were shown to detect a failure, and repeated runs were consistent. Link the evidence.
- **VALIDATION FAILED:** the check could not run, did not assert as designed, or gave inconsistent results across runs (for example flaky behavior). Record the failure and evidence.
- **NOT VALIDATED:** the check was written but not run, with the reason (for example not authorized, environment or revision unavailable, or a blocking open question).

Validation status describes the automation, not the product. A VALIDATED check that reports a product failure is a working check; record the observed result and point it to the execution skills and `triage-defects` (A34). Do not count validation runs as executed test results.

Before delivery, check that every selected test ID is automated or listed with its reason, each check traces to its A16 case and asserts its designed expected result, fixtures use A18 resources by reference, the run command and configuration are complete, every validation status has evidence or a reason, and no case, expected result, command or credential was invented.

## Output: A19 — Test Automation Outputs

When working in this project, read and follow the [A19 template](../../../AIAugmentation/templates/A19_test-automation-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A19_test-automation-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Preparation/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep test code, fixtures, configuration and result files in their native formats in the project's test locations and link them.

Include a short header with the feature, A19 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `code_revision`, `test_ids`, `suite_type`, `fixtures`, `command`, `config_refs` and `validation_results`, referencing the child sections or native files rather than duplicating them. Then use these stable sections:

- **A19-01 — Automated test code and reusable fixtures:** One row per test ID with its requirement and criterion links, suite type, test file and test name or tag, and the fixtures, stubs and A18 datasets it uses, followed by the reusable fixtures and the excluded candidates with reasons.
- **A19-02 — Execution configuration and reporting integration:** The run commands per suite, configuration files and environment variables by name, tags or selection rules, the result format and location, exit-code behavior and how results map to test IDs, builds and code revisions for the execution and progress skills.
- **A19-03 — Setup guide and automation validation results:** The setup guide, then one row per check with its validation status, code revision, environment, command, run date, native result path and checksum, the failure-detection evidence and repeat-run consistency, with product results observed during validation noted for handoff.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native test code, configuration and validation result files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A19-01 through A19-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` and VALIDATED statuses are not executed test results, acceptance of the product or test-exit approval. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts and native files are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files, existing tests and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Preserve test IDs and the names or tags that map checks to them. When a revision follows changed cases, a new code revision or a validation failure, list the affected checks, re-validate them rather than carrying a VALIDATED status forward, and keep the earlier validation results visible. For each prior finding or failed validation, state whether it was fixed, retained with explanation or blocked pending clarification.

Finish with a link to A19, the validation counts and the open decisions. A19 can be passed to `execute-smoke-tests` (A27), `execute-integration-tests` (A28) and `execute-regression-tests` (A31). Invoke those skills only when the user's scope includes that work. Do not automatically run the formal test campaign, triage or fix defects, commit or push code, change CI pipelines, approve test exit or publish results externally.

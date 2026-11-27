# build-test-automation — User guide

Use this skill to turn selected designed test cases into runnable automated checks, or revise them after the cases, code revision or validation results change. It produces **A19 — Test Automation Outputs**: automated test code and reusable fixtures, execution configuration and reporting integration, and a setup guide with recorded automation validation. The smoke, integration and regression execution skills read it. It does not change application code, run the formal test campaign, fix or triage defects, or approve test exit.

## What you need

The minimum input is designed test cases with expected results, a selection of cases to automate (the A16 automation candidates or test IDs you name) and the project's test framework and location. Supply them as documents, existing code or text; no particular filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A16 | `A16_test-case-creation-outputs` | Designed cases, expected results and automation candidates |
| A17 | `A17_test-coverage-review-outputs` | Coverage review status and findings for those cases |
| A09 | `A09_system-component-design-outputs` | Components and interfaces under test |
| E05 | `E05_repository-and-ci-evidence` | Repository revision, framework, conventions and CI evidence |
| A18 | `A18_test-resources-outputs` | Datasets, environment and setup to reuse |
| A15 | `A15_test-planning-outputs` | Planned test levels and responsibilities |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A18_test-resources-outputs_ITER-001_v1.0.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files may be absent without preventing a useful draft. Missing frameworks, commands, revisions or expected results become explicit open items, not invented values.

## Before you build automation

The skill writes test code, fixtures and configuration in the project's existing test locations and conventions, and never changes application code or weakens existing tests. It validates the automation only when your request asks for it, using the command and environment you or the project instructions identify. Put the framework, test location and run commands in the project's `AGENTS.md` or in the optional guide. Without them, it asks or marks checks NOT VALIDATED with the reason. It does not add a new framework or CI pipeline without your agreement, and it does not commit, push, deploy or file defects.

## Use the skill

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $build-test-automation with [A16 file] for the automation candidates.

Use $build-test-automation with [A16 file] for [test IDs] on revision [code revision] and validate it with [command].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

If the skill is not recognized, use:

```text
Read and follow .agents/skills/build-test-automation/SKILL.md with [inputs].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
frameworks, test directories, naming, tags, commands, reporting formats and output conventions, use the optional
`AIAugmentation/project_guides/build-test-automation-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A19_test-automation-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Preparation/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A19 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. The A19 document remains Markdown; test code, configuration and result files stay in their native formats in the project's test locations and are linked.

| Section | Contents |
| --- | --- |
| A19-01 | Automated checks per test ID with suite type, file and test name, fixtures and A18 datasets used, and excluded candidates |
| A19-02 | Run commands, configuration, selection tags, result format and how results map to test IDs and revisions |
| A19-03 | Setup guide and validation status per check with revision, environment, command, result file and evidence |

Each automated check is VALIDATED, VALIDATION FAILED or NOT VALIDATED. VALIDATED needs evidence that the check ran on the recorded revision, detects a failure and repeats consistently. Validation describes the automation, not the product: validation runs are not executed test results. The document status stays **DRAFT**; it is not test-exit approval.

The project uses the [A19 template](../../../AIAugmentation/templates/A19_test-automation-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $build-test-automation to revise [A19 file] using [changed A16, A17 findings, new code revision or validation results].
```

The skill preserves source files, prior outputs, existing tests and test IDs. A revision re-validates affected checks instead of carrying VALIDATED forward, and keeps earlier validation results visible.

Pass the resulting A19 to [execute-integration-tests](../execute-integration-tests/README.md) or [execute-regression-tests](../execute-regression-tests/README.md), or to `execute-smoke-tests` when it is available, when you ask for that work:

```text
Use $execute-regression-tests with [A19 file] on build [build ID] in [environment].
```

Each step happens when you request it, rather than starting an automatic loop.

## Check the result

Confirm that every selected test is automated or listed with its reason, each check traces to its designed case and asserts its expected result, fixtures reuse A18 resources, the run command and configuration are complete, every validation status has evidence or a reason, and input files remain unchanged. Human owners keep the test-exit decision.

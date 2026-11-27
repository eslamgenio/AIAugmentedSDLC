# execute-regression-tests — User guide

Use this skill to select the existing tests that a build's changes could affect, run them, or record a run that already happened. It produces **A31 — Regression Testing Outputs**: the selected scope with its rationale, results with evidence and build ID, new failures, excluded coverage and residual risks. It does not design cases, fix or triage defects, or approve test exit.

## What you need

The minimum input is the changes in a build, the existing tests to select from, the build ID and an environment you are authorized to test. Supply them as documents, tool exports or text; no particular filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A16 | `A16_test-case-creation-outputs` | Designed cases available for selection |
| A17 | `A17_test-coverage-review-outputs` | Coverage review status and known gaps |
| A19 | `A19_test-automation-outputs` | Automated checks and how to run them |
| E06 | `E06_test-and-defect-baselines` | Existing regression suites and defects |
| A20 | `A20_feature-implementation-outputs` | Implemented changes |
| A22 | `A22_code-review-outputs` | Reviewed changes and their impact |
| A35 | `A35_defect-fix-outputs` | Defect fixes in the build |
| A18 | `A18_test-resources-outputs` | Test data and environment preparation |
| A26 | `A26_test-deployment-outputs` | Deployed build and test environment identity |
| E07 | `E07_environment-and-access-records` | Environment availability and access |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A16_test-case-creation-outputs_ITER-001_v1.0.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files may be absent without preventing a useful draft. Missing builds, environments, targets or decisions become explicit open items, not invented values.

## Before you run tests

The skill runs tests only when your request asks for execution, and only against the build, environment, data and commands you or the project instructions identify. Put the commands in the project's `AGENTS.md` or in the optional guide. Without that, it records a supplied run or marks tests NOT RUN with the reason. It never deploys, rebuilds, changes code or test assets, runs against production, or files defects in a tracker.

## Use the skill

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $execute-regression-tests for build [build ID] with changes [change records] and tests [A16 file or suite].

Use $execute-regression-tests to record the results in [results file or folder] for build [build ID].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

If the skill is not recognized, use:

```text
Read and follow .agents/skills/execute-regression-tests/SKILL.md with [inputs].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
commands, environments, tools, identifiers and output conventions, use the optional
`AIAugmentation/project_guides/execute-regression-tests-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A31_regression-testing-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Execution/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A31 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown, and native evidence such as logs and result files stays in its own format and is linked.

| Section | Contents |
| --- | --- |
| A31-01 | Suite ID, change impact and the selected tests with their rationale |
| A31-02 | Results per selected test with build, status and evidence |
| A31-03 | New failures, excluded coverage, gaps and residual risks |

Each selected test is PASSED, FAILED, BLOCKED or NOT RUN. Failures are marked as new, known or previously passing, and exclusions stay visible as residual risk. The document status stays **DRAFT**; it is not human approval or test exit.

The project uses the [A31 template](../../../AIAugmentation/templates/A31_regression-testing-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $execute-regression-tests to re-run [A31 file] on build [new build ID] with changes [change records].
```

The skill preserves source files, prior outputs and existing IDs. Each run or reassessment is a new version, so earlier results stay visible.

Pass new failures to `triage-defects`, and the results to `report-test-progress` and `assess-test-readiness`, when those skills are available and you ask for that work. Each step happens when you request it, rather than starting an automatic loop.

## Check the result

Confirm that every selected test traces to a change or risk, exclusions and gaps are explicit, and every result names its build. Human owners keep the test-exit decision.

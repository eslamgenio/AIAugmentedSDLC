# report-test-progress — User guide

Use this skill to report where testing stands for a reporting period, from the execution records you already have. It produces **A32 — Test Progress Outputs**: planned and executed counts, status counts that reconcile to the records, coverage, defects, blockers, forecast risks and next actions. It does not run tests, change results or approve test exit.

## What you need

The minimum input is one or more execution records with statuses per test and build, and the reporting period you want covered. Supply them as documents, tool exports or text; no particular filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A27 | `A27_smoke-testing-outputs` | Smoke test results |
| A28 | `A28_integration-testing-outputs` | Integration test results, from [execute-integration-tests](../execute-integration-tests/README.md) |
| A29 | `A29_functional-testing-outputs` | Functional test results, from [execute-functional-tests](../execute-functional-tests/README.md) |
| A30 | `A30_nonfunctional-testing-outputs` | Non-functional results, from [execute-nonfunctional-tests](../execute-nonfunctional-tests/README.md) |
| A31 | `A31_regression-testing-outputs` | Regression results, from [execute-regression-tests](../execute-regression-tests/README.md) |
| A36 | `A36_defect-retest-outputs` | Defect retest results |
| A15 | `A15_test-planning-outputs` | Planned scope, schedule and criteria |
| A34 | `A34_defect-triage-outputs` | Defect status and severity |
| E06 | `E06_test-and-defect-baselines` | Defect register and status definitions |
| A17 | `A17_test-coverage-review-outputs` | Coverage and known gaps |
| E04 | `E04_delivery-planning-records` | Delivery milestones and dates |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A27_smoke-testing-outputs_ITER-001_v1.0.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files may be absent without preventing a useful draft. Missing builds, environments, targets or decisions become explicit open items, not invented values.

## What this skill does not do

The skill works only from existing records. It does not run tests, change or re-classify results, or fill in missing evidence. Gaps and conflicts in the records stay visible in the output.

## Use the skill

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $report-test-progress for [reporting period] with [execution records or folder].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

If the skill is not recognized, use:

```text
Read and follow .agents/skills/report-test-progress/SKILL.md with [inputs].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
commands, environments, tools, identifiers and output conventions, use the optional
`AIAugmentation/project_guides/report-test-progress-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A32_test-progress-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Execution/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A32 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown, and native evidence such as logs and result files stays in its own format and is linked.

| Section | Contents |
| --- | --- |
| A32-01 | Reporting period, build scope, status definitions and reconciled counts |
| A32-02 | Coverage, defects and blockers |
| A32-03 | Forecast risks and recommended next actions |

Counts are per build and per test level, with unique tests distinguished from executions. Planned equals executed plus blocked plus not run for each build, or the difference is explained. The document status stays **DRAFT**; it is not human approval or test exit.

The project uses the [A32 template](../../../AIAugmentation/templates/A32_test-progress-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $report-test-progress for [next reporting period] using [prior A32 file] and [new execution records].
```

The skill preserves source files, prior outputs and existing IDs. Each run or reassessment is a new version, so earlier results stay visible.

Pass the report and the execution records to `assess-test-readiness` when you want the exit assessment. Each step happens when you request it, rather than starting an automatic loop.

## Check the result

Confirm that every count traces to an execution record, builds and periods are not mixed silently, and no date or owner was invented. Human owners keep the test-exit decision.

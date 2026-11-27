# assess-test-readiness — User guide

Use this skill to assess a candidate build against the test plan's exit criteria before the human test-exit decision. It produces **A33 — Test Exit Assessment Outputs**: a result for every criterion with its evidence, the gaps and residual risks, and a READY or NOT READY recommendation. It does not run tests, waive criteria or grant test-exit approval.

## What you need

The minimum input is the exit criteria, the candidate build and the execution evidence for that build. Supply them as documents, tool exports or text; no particular filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A15 | `A15_test-planning-outputs` | Exit criteria, from [plan-testing](../plan-testing/README.md) |
| E09 | `E09_human-decisions` | Recorded decisions and waivers |
| A17 | `A17_test-coverage-review-outputs` | Coverage and known gaps |
| A27 | `A27_smoke-testing-outputs` | Smoke test results |
| A28 | `A28_integration-testing-outputs` | Integration test results |
| A29 | `A29_functional-testing-outputs` | Functional test results |
| A30 | `A30_nonfunctional-testing-outputs` | Non-functional results |
| A31 | `A31_regression-testing-outputs` | Regression results |
| A34 | `A34_defect-triage-outputs` | Defect status and severity |
| A36 | `A36_defect-retest-outputs` | Defect retest results |
| E06 | `E06_test-and-defect-baselines` | Defect register and thresholds |
| A06 | `A06_feasibility-assessment-outputs` | Risk register |
| A32 | `A32_test-progress-outputs` | Progress report, from [report-test-progress](../report-test-progress/README.md) |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A15_test-planning-outputs_ITER-001_v1.0.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files may be absent without preventing a useful draft. Missing builds, environments, targets or decisions become explicit open items, not invented values.

## What this skill does not do

The skill works only from existing records. It does not run tests, change or re-classify results, or fill in missing evidence. Gaps and conflicts in the records stay visible in the output.

## Use the skill

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $assess-test-readiness for candidate [candidate or build ID] with [A15 file] and [evidence folder].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

If the skill is not recognized, use:

```text
Read and follow .agents/skills/assess-test-readiness/SKILL.md with [inputs].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
commands, environments, tools, identifiers and output conventions, use the optional
`AIAugmentation/project_guides/assess-test-readiness-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A33_test-exit-assessment-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Execution/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A33 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown, and native evidence such as logs and result files stays in its own format and is linked.

| Section | Contents |
| --- | --- |
| A33-01 | Every exit criterion with its result (MET, NOT MET or PENDING) and cited evidence |
| A33-02 | Unmet and pending criteria, gaps and residual risks |
| A33-03 | READY or NOT READY recommendation and the evidence for the human gate |

READY means every exit criterion is met, or waived by a recorded human decision, with evidence on the candidate build. Anything else is NOT READY, with the criteria and actions that would change it. The document status stays **DRAFT**; it is not human approval or test exit.

The project uses the [A33 template](../../../AIAugmentation/templates/A33_test-exit-assessment-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $assess-test-readiness to reassess [A33 file] with [new evidence or candidate build].
```

The skill preserves source files, prior outputs and existing IDs. Each run or reassessment is a new version, so earlier results stay visible.

The human test owner makes the exit decision and records it in E09. On NOT READY, pass the gaps to `triage-defects` or the relevant test skill; after a recorded exit decision, A33 can go to `summarize-test-results` when that skill is available. Each step happens when you request it, rather than starting an automatic loop.

## Check the result

Confirm that every exit criterion is assessed with evidence from the candidate build, waivers are cited from E09, and the recommendation follows from the results. The recommendation is not test-exit approval; human owners keep that decision.

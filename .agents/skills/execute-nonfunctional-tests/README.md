# execute-nonfunctional-tests — User guide

Use this skill to measure the quality attributes your requirements, policies or risks call for, such as performance, reliability, security, accessibility or usability, or to record a run that already happened. It produces **A30 — Nonfunctional Testing Outputs**: measurements against sourced targets with the workload, tools and environment, limitations and findings. It does not invent thresholds, run load or security tests against targets you have not authorized, or approve test exit.

## What you need

The minimum input is a non-functional requirement, policy or risk with a measurable target, an identified build and an environment you are authorized to test this way. Supply them as documents, tool exports or text; no particular filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A15 | `A15_test-planning-outputs` | Non-functional scope and criteria |
| A06 | `A06_feasibility-assessment-outputs` | Quality risks |
| E03 | `E03_engineering-and-governance-policies` | Quality and security policies |
| E06 | `E06_test-and-defect-baselines` | Targets, workloads and baselines |
| A18 | `A18_test-resources-outputs` | Test data, tools and environment preparation |
| E05 | `E05_repository-and-ci-evidence` | Build provenance and CI evidence |
| E07 | `E07_environment-and-access-records` | Environment size, availability and access |
| E08 | `E08_operational-and-product-evidence` | Existing operational measurements |
| A26 | `A26_test-deployment-outputs` | Deployed build and test environment identity |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A15_test-planning-outputs_ITER-001_v1.0.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files may be absent without preventing a useful draft. Missing builds, environments, targets or decisions become explicit open items, not invented values.

## Before you run tests

The skill runs tests only when your request asks for execution, and only against the build, environment, data and commands you or the project instructions identify. Put the commands in the project's `AGENTS.md` or in the optional guide. Without that, it records a supplied run or marks tests NOT RUN with the reason. It never deploys, rebuilds, changes code or test assets, runs against production, or files defects in a tracker.

## Use the skill

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $execute-nonfunctional-tests with [A15 file] on build [build ID] in [environment].

Use $execute-nonfunctional-tests to record the measurements in [results file or folder] for build [build ID].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

If the skill is not recognized, use:

```text
Read and follow .agents/skills/execute-nonfunctional-tests/SKILL.md with [inputs].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
commands, environments, tools, identifiers and output conventions, use the optional
`AIAugmentation/project_guides/execute-nonfunctional-tests-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A30_nonfunctional-testing-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Execution/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A30 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown, and native evidence such as logs and result files stays in its own format and is linked.

| Section | Contents |
| --- | --- |
| A30-01 | Measurements per category compared with their sourced targets |
| A30-02 | Workload, tools, configuration, observations, limitations and omitted categories |
| A30-03 | Findings, defect candidates and tuning recommendations |

Each measurement is PASSED, FAILED, BLOCKED or NOT RUN against its target. An excluded category is NOT APPLICABLE with its source, and a measurement without a target is MEASURED — NO TARGET, never PASSED. The document status stays **DRAFT**; it is not human approval or test exit.

The project uses the [A30 template](../../../AIAugmentation/templates/A30_nonfunctional-testing-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $execute-nonfunctional-tests to re-run [A30 file] on build [new build ID].
```

The skill preserves source files, prior outputs and existing IDs. Each run or reassessment is a new version, so earlier results stay visible.

Pass failed targets to `triage-defects`, and the results to `report-test-progress` and `assess-test-readiness`, when those skills are available and you ask for that work. Each step happens when you request it, rather than starting an automatic loop.

## Check the result

Confirm that every measurement names its workload, tool, build, environment and target, no threshold was invented, and omitted categories are justified. Human owners keep the test-exit decision.

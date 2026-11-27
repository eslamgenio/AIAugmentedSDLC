# plan-testing — User guide

Use this skill to turn a requirements baseline into a scoped, risk-based test plan, or revise an existing plan after feedback or a baseline change. It produces **A15 — Test Planning Outputs**, which [create-test-cases](../create-test-cases/README.md) reads as its test scope and strategy. It does not design test cases, execute tests or approve test exit.

## What you need

The minimum input is requirements that describe the intended behavior and scope, ideally with acceptance criteria. Supply them as a document or text. An A05 bundle may embed the baseline or reference an accessible source; no particular requirements filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A05 | `A05_requirements-review-outputs` | Requirements baseline, embedded or referenced, and review gate |
| A04 | `A04_acceptance-criteria-outputs` | Acceptance criteria |
| A02 | `A02_scope-definition-outputs` | Scope boundaries, exclusions and deferrals |
| E09 | `E09_human-decisions` | Actual decisions or pending agreement |
| A06 | `A06_feasibility-assessment-outputs` | Risk register |
| A09 | `A09_system-component-design-outputs` | Design and logical interfaces that shape test levels |
| A14 | `A14_iteration-planning-outputs` | Milestones and dates |
| E06 | `E06_test-and-defect-baselines` | Test policy, coverage rules and defect thresholds |
| E03 | `E03_engineering-and-governance-policies` | Quality and governance policies |
| E07 | `E07_environment-and-access-records` | Environment and access availability |
| E01 | `E01_business-context` | Business and domain rules |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A05_requirements-review-outputs_ITER-001_v1.1.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files and formal approval may be absent without preventing a useful draft. Missing dates, owners, environments or thresholds become explicit open items, not invented values.

## Create a plan

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $plan-testing with [requirements file or folder].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

No Python or application runtime is required. If the skill is not recognized, use:

```text
Read and follow .agents/skills/plan-testing/SKILL.md with [requirements file or folder].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
test levels, environments, owners, thresholds and output conventions, use the optional
`AIAugmentation/project_guides/plan-testing-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A15_test-planning-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Preparation/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A15 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown.

| Section | Contents |
| --- | --- |
| A15-01 | Plan ID, objective, in-scope requirement/criterion IDs, exclusions, risk-based priorities and approach |
| A15-02 | Test levels and types, activity/role/owner responsibilities, sequence and dates, environment and data needs |
| A15-03 | Measurable entry, exit and suspension/resumption criteria with evidence sources and status |

The plan's document status is **DRAFT** until a human owner records agreement. Pending approval, unassigned owners, missing dates and unverified environments remain visible in the plan rather than being filled in.

The project uses the [A15 template](../../../AIAugmentation/templates/A15_test-planning-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $plan-testing to revise [A15 file] using [changed baseline, review findings or feedback].
```

The skill preserves source files, prior outputs, the plan ID and IDs for unchanged criteria and items. A revision such as v1.1 records what changed and lists affected requirements so downstream cases can be rechecked.

Pass the resulting A15 and the same baseline to [create-test-cases](../create-test-cases/README.md):

```text
Use $create-test-cases with [requirements file or folder].
```

Test design, coverage review and further revisions happen when requested, rather than starting an automatic loop.

## Check the result

Confirm that source versions are identified, every in-scope requirement and criterion is accounted for, risks link to requirements, every entry, exit and suspension criterion can be checked as met or not met, and input files remain unchanged. Human owners keep the approval and test-exit decisions.

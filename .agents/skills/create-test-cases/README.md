# create-test-cases — User guide

Use this skill to turn requirements into reviewable test cases, or revise existing cases after feedback. It produces **A16 — Test Case Creation Outputs**. It does not execute application tests.

## What you need

The minimum input is requirements that describe the intended behavior and scope. Supply them as a document or text. In this project, **A05 v1.1 embeds the complete sample baseline**; no separate requirements file is necessary.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A05 | `A05_requirements-review-outputs` | Requirements baseline, embedded or referenced |
| A04 | `A04_acceptance-criteria-outputs` | Acceptance criteria |
| A15 | `A15_test-planning-outputs` | Test scope and strategy |
| A06 | `A06_feasibility-assessment-outputs` | Risks and feasibility |
| A09 | `A09_system-component-design-outputs` | Design and logical interfaces |
| E06 | `E06_test-and-defect-baselines` | Case format and coverage rules |
| E01 | `E01_business-context` | Business and domain rules |
| E09 | `E09_human-decisions` | Actual decisions or pending agreement |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A05_requirements-review-outputs_ITER-001_v1.1.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files and formal approval may be absent without preventing a useful draft. Missing essential behavior becomes a question, not an invented expected result.

## Create cases

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $create-test-cases with dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md.
```

The skill should discover the supporting inputs without listing them again in your prompt. For an isolated practice run, append:

```text
Save the output under dummy/runs/create-test-cases/ITER-001/.
```

No Python or application runtime is required. If the skill is not recognized, use:

```text
Read and follow .agents/skills/create-test-cases/SKILL.md with dummy/ITER-001/A05_requirements-review-outputs_ITER-001_v1.1.md.
```

## What you receive

By default, the first output is `artifacts/ITER-001/A16_test-case-creation-outputs_ITER-001_v1.0.md`, using the selected iteration. A supplied output location takes precedence. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

| Section | Contents |
| --- | --- |
| A16-01 | Requirement-linked cases with IDs, preconditions, data, numbered steps and observable expected results |
| A16-02 | Setup/data summary and references to expected results |
| A16-03 | Questions, automation candidates, scope accounting and revision responses where applicable |

A case marked **READY FOR REVIEW** has defined expectations; **BLOCKED** means a linked question prevents completing its expectations. Neither means a test passed. The number of cases depends on the required behavior, not a fixed target.

The project uses the [A16 template](../../../templates/A16_test-case-creation-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $create-test-cases to revise [A16 file] using [A17 file].
```

The creator preserves source files, prior outputs and IDs for unchanged logical cases. A revision such as v1.1 records what changed and responds to the findings; it does not independently verify their closure.

Pass the resulting A16 and the same baseline to [review-test-coverage](../review-test-coverage/README.md). Review and further revisions happen when requested, rather than starting an automatic loop.

## Check the result

Confirm that source versions are identified, every requirement/criterion is accounted for, expectations follow the source, and input files remain unchanged. Check unresolved questions before using the cases. Pending approval and unverified execution environments must remain visible.

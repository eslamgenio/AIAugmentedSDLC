# prepare-test-resources — User guide

Use this skill to prepare the test data and environment resources that designed test cases need, or revise them after the cases or environment change. It produces **A18 — Test Resources Outputs**: permitted synthetic or masked datasets, environment setup scripts or a configuration checklist, and a readiness record with evidence and a cleanup procedure. [build-test-automation](../build-test-automation/README.md) and the execution skills read it. It does not design cases, provision shared environments without authorization, use real personal data, execute tests or approve test entry.

## What you need

The minimum input is designed test cases with their preconditions and data needs, ideally an A16 bundle. Supply them as a document or text; no particular filename is mandatory.

Keep relevant supporting inputs together in the selected iteration folder. The skill reads these when present:

| Artifact | Canonical filename prefix | What it supplies |
| --- | --- | --- |
| A16 | `A16_test-case-creation-outputs` | Designed cases, preconditions and data needs |
| E02 | `E02_product-and-architecture-context` | Data model, components and configuration context |
| E03 | `E03_engineering-and-governance-policies` | Data-handling, masking and governance rules |
| E07 | `E07_environment-and-access-records` | Environment identity, availability and access |
| A15 | `A15_test-planning-outputs` | Planned environment and data needs |

Append `_{iteration_id}_v{artifact_version}.md` to each prefix. For example, `A16_test-case-creation-outputs_ITER-001_v1.0.md`. Explicitly supplied versions take precedence; otherwise the skill uses compatible current versions in the selected iteration. Optional supporting files may be absent without preventing a useful draft. Missing data rules, environments, accounts or permissions become explicit open items, not invented values.

## Before you prepare resources

The skill prefers synthetic data and uses masked data only from a source and rule that you or E03 permit. It never copies real personal data, production records, secrets or credentials into datasets, scripts or evidence. It writes datasets, scripts and checklists as new project files and runs setup or verification steps only when your request asks for them, against an environment you or the project instructions identify. Put the location, environment and commands in the project's `AGENTS.md` or in the optional guide. Without that, it provides the scripts or checklist and marks readiness UNVERIFIED. It never provisions, resets or deletes shared or production resources without your explicit authorization.

## Use the skill

Open the project in Codex and start a task. Example prompts use paths relative to the project root:

```text
Use $prepare-test-resources with [A16 file] for [environment].

Use $prepare-test-resources with [A16 file] for [environment] and verify readiness using [command or procedure].
```

The skill should discover the supporting inputs without listing them again in your prompt. To choose a different output location, append:

```text
Save the output under [output folder].
```

No Python or application runtime is required for the skill itself. If the skill is not recognized, use:

```text
Read and follow .agents/skills/prepare-test-resources/SKILL.md with [inputs].
```

Replace bracketed placeholders with your actual project paths. Sample artifacts
are not installation requirements.

## Project-specific conventions

Keep shared project context in the project's `AGENTS.md`. For activity-specific
data rules, masking methods, environments, resource locations, commands and output conventions, use the optional
`AIAugmentation/project_guides/prepare-test-resources-guide.md`.
The skill checks this guide before working and continues with its generic
workflow when it is absent. Guides cannot override higher-priority instructions,
explicit user requests, authorization boundaries or the skill's fixed scope.
Keep reusable procedures in `SKILL.md` rather than modifying them for each project.

## What you receive

Without a configured layout, the first output is `AIAugmentation/artifacts/ITER-001/A18_test-resources-outputs_ITER-001_v1.0.md`, using the selected iteration. With phase layout, it goes under that iteration's `Test Preparation/` folder. A supplied output location takes precedence; revisions otherwise stay in the prior A18 folder. Existing files are preserved; revisions receive new versions. Output versions are independent of input versions.

Input discovery includes the active iteration root and its subfolders, including other phases and `External Inputs/`. Explicit paths and versions take precedence. Duplicate artifact/version candidates or conflicting baselines need clarification before the affected input is used; files from other iterations are used only when explicitly supplied or referenced. Outputs remain Markdown, and datasets, scripts and configuration stay in their native formats and are linked.

| Section | Contents |
| --- | --- |
| A18-01 | Datasets with the test IDs they serve, file paths, generation or masking method, permitted-use basis and checksums |
| A18-02 | Environment ID, configuration version, setup scripts or checklist, components, accounts by reference and stubs |
| A18-03 | Readiness status and evidence per resource, and the ordered cleanup procedure |

Each dataset, setup item and prerequisite is READY, NOT READY or UNVERIFIED. READY needs linked evidence from the identified environment; NOT READY names the obstacle; UNVERIFIED gives the reason it was not checked. The document status stays **DRAFT**; READY resources are not test-entry approval.

The project uses the [A18 template](../../../AIAugmentation/templates/A18_test-resources-outputs.md). When the skill is copied without project templates, it uses the built-in layout in [SKILL.md](SKILL.md).

## Revise and hand off

Replace the bracketed file references with your actual paths:

```text
Use $prepare-test-resources to revise [A18 file] using [changed A16, environment record or feedback].
```

The skill preserves source files, prior outputs, datasets and existing IDs. A revision re-verifies readiness instead of carrying READY forward and lists the affected test IDs so automation and execution can be rechecked.

Pass the resulting A18 to [build-test-automation](../build-test-automation/README.md) or to an execution skill such as [execute-functional-tests](../execute-functional-tests/README.md) when you ask for that work:

```text
Use $build-test-automation with [A16 file] and [A18 file].
```

Each step happens when you request it, rather than starting an automatic loop.

## Check the result

Confirm that every in-scope test's data and setup needs are covered or listed as gaps, every dataset has a permitted-use basis and contains no real personal data or secrets, every readiness status has evidence or a reason, cleanup is defined, and input files remain unchanged. Human owners keep the test-entry decision.

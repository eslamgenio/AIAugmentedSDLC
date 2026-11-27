---
name: prepare-test-resources
description: DSK Prepare or revise the test data and environment resources that designed tests need, with permitted synthetic or masked datasets, environment setup scripts or configuration checklists, a readiness record with evidence and a cleanup procedure. Produces the A18 test-resources bundle consumed by test automation and execution; does not provision shared environments without authorization, use real personal data, execute tests or approve test entry.
---

# Prepare test resources

Turn the designed test cases into the data and environment resources a tester or an automation engineer needs before execution, and show with evidence which resources are ready. Work across domains and technologies; choose data, setup and checks appropriate to the supplied feature. No custom runner or other skill is required; use the project's own tools.

## Optional project guide

Before preparing test resources, look for `AIAugmentation/project_guides/prepare-test-resources-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, data-handling rules, environments, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization, data-protection and test-preparation boundaries.

## Inputs and scope

- Read the designed test cases and their setup and data needs (A16, especially A16-02), the product and architecture context that shapes data and configuration (E02), the engineering, governance and data-handling policies (E03), and the environment and access records (E07). Use the plan's environment and data needs (A15-02) as context when available. Files, pasted text and existing project documents are acceptable. Preserve source IDs and versions where provided.
- If no designed cases or data needs can be identified, ask for them. Do not invent data rules, field formats, value ranges, environments, accounts or configuration values. Record a targeted question or an explicit `Missing — impact / owner` entry and continue with the resources that do not depend on it.
- Prepare only the resources the designed cases need. Note a case whose data or setup cannot be derived from its source as an open item rather than changing the case; test design belongs to `create-test-cases`.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the designed cases and their data and setup needs from A16, product and architecture context from E02, data-handling and governance rules from E03, and environment identity, availability and access from E07. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A16_test-case-creation-outputs_{iteration_id}_v{artifact_version}.md`
- `E02_product-and-architecture-context_{iteration_id}_v{artifact_version}.md`
- `E03_engineering-and-governance-policies_{iteration_id}_v{artifact_version}.md`
- `E07_environment-and-access-records_{iteration_id}_v{artifact_version}.md`
- `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`

For revisions, also read the supplied prior `A18_test-resources-outputs_{iteration_id}_v{artifact_version}.md` and the changed cases, policies, environment records or feedback that prompted the revision.

## Data-protection and environment boundary

- Prefer synthetic data. Use masked or anonymized data only when the user or E03 identifies a permitted source and masking rule, and record the rule applied. Never copy real personal data, production records, secrets or credentials into a dataset, script, artifact or evidence; when a case seems to need them, record the gap and the decision needed instead.
- Write datasets, setup scripts, configuration files and checklists as native project files in the location identified by the user, the project instructions or the optional guide; otherwise next to the A18 output. Do not overwrite existing test data, fixtures or configuration; create new versioned files and link them.
- Run setup, seed or verification steps only when the user's request includes them, and only against an environment identified by the user, the project instructions, the optional guide or E07. Do not provision, reconfigure, reset or delete shared or production environments, accounts or data unless the user explicitly authorizes that target and the project rules allow it. Otherwise provide the script or checklist and mark its readiness UNVERIFIED.
- Stay within resource preparation. Do not change application code, deploy builds, execute the designed tests, request access on someone's behalf or publish resources externally. Reference credentials and secrets by their managed location or variable name, never by value, and redact them from copied evidence.

## Prepare the resources

1. **Pin the basis.** Record the exact A16 revision and the test IDs in scope, and the E02, E03, E07 and A15 revisions used. Give the environment a stable `env_id` from E07 or the project; when none exists, record the gap rather than naming one.
2. **Derive the data needs.** For each test ID, list the data it needs: entities, states, boundary and invalid values, volumes and relationships, traced to its preconditions, steps and expected results. Group shared needs into datasets with stable IDs (for example `DS-###`), and record which test IDs use each one.
3. **Create the datasets.** Generate synthetic records, or apply the identified masking rule, so that every value the designed expected results depend on is present and representative. Record each dataset's native file path, format, generation or masking method, permitted-use basis from E03 or the user, and checksum or revision. Do not alter expected results to fit convenient data.
4. **Define the environment setup.** Describe the configuration and setup the tests need: components and versions, configuration values, accounts or roles, stubs or simulators, tools and seed steps. Provide an idempotent setup script where the project's tooling supports it, otherwise a numbered configuration checklist, with a stable `config_version`. Mark which items come from E07 or E02 and which are proposed.
5. **Check readiness.** For each resource, record whether it is ready and the evidence: a verification command and its output, an E07 record or a supplied confirmation. Do not claim readiness from a script or checklist alone.
6. **Define cleanup.** Give the steps to reset or remove data, accounts, stubs and configuration after execution, with their order and any data that must be preserved. Mark cleanup steps that were not run as not run.

Use these readiness statuses for every dataset, setup item and environment prerequisite, and define them in the artifact:

- **READY:** prepared or available, and verified with linked evidence in the identified environment.
- **NOT READY:** checked, and a named obstacle prevents use, such as missing access, an unavailable dependency, a failed verification or an unresolved data-permission decision. Link the obstacle.
- **UNVERIFIED:** prepared or described but not checked in the identified environment, with the reason (for example not authorized, environment unreachable or no environment identified).

READY means the resource can support execution; it is not test-entry approval. Do not infer READY from a script, checklist or E07 entry that predates the build or configuration under test.

Before delivery, check that every in-scope test ID's data and setup needs are covered or listed as gaps, every dataset has a permitted-use basis and contains no real personal data or secrets, every readiness status has evidence or a reason, cleanup is defined, and no data rule, environment, account or configuration value was invented.

## Output: A18 — Test Resources Outputs

When working in this project, read and follow the [A18 template](../../../AIAugmentation/templates/A18_test-resources-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A18_test-resources-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Preparation/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep datasets, scripts and configuration in their native formats and link them.

Include a short header with the feature, A18 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `dataset_refs`, `env_id`, `config_version`, `setup_refs`, `readiness` and `cleanup_steps`, referencing the child sections or native files rather than duplicating them. Then use these stable sections:

- **A18-01 — Synthetic or masked test datasets:** One row per dataset ID with the test IDs it serves, native file path and format, generation or masking method, permitted-use basis, checksum or revision and limitations, followed by a test-ID-to-dataset map and any test IDs whose data needs remain gaps.
- **A18-02 — Environment setup scripts or configuration checklist:** The `env_id`, `config_version`, the setup script paths or numbered checklist items, components and versions, accounts or roles by reference, stubs or simulators and the side each replaces, with the source of each item or its proposed status.
- **A18-03 — Resource readiness record and cleanup procedure:** One row per dataset, setup item and prerequisite with its readiness status, check performed, evidence path and date, followed by the ordered cleanup steps and whether each was run.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native dataset, script and verification files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A18-01 through A18-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` and READY resource statuses are not test-entry approval. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts and native files are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files, native resources and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source, dataset, script or prior version.

Preserve dataset IDs, the `env_id` and the IDs of unchanged setup items. Assign new IDs to new resources; record removed or superseded resources without reusing their IDs, and increment `config_version` when the configuration changes. When a revision follows changed cases or a changed environment, list the affected test IDs and resources so dependent automation and execution can be rechecked, and re-verify readiness rather than carrying a READY status forward.

Finish with a link to A18, the readiness counts and the open decisions. A18 can be passed to `build-test-automation` (A19) and to the execution skills, such as `execute-integration-tests` (A28), `execute-functional-tests` (A29), `execute-nonfunctional-tests` (A30) and `execute-regression-tests` (A31). Invoke those skills only when the user's scope includes that work. Do not automatically build automation, execute tests, provision environments, approve test entry or publish resources externally.

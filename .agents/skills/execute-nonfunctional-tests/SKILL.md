---
name: execute-nonfunctional-tests
description: DSK Execute or record relevant non-functional tests such as performance, reliability, security, accessibility or usability against sourced quality targets, with the workload, tools, build, environment, measurements, limitations and findings. Produces the A30 non-functional testing bundle; does not invent thresholds, run unauthorized load or security tests, or approve test exit.
---

# Execute non-functional tests

Measure the quality attributes the requirements, policies or risks call for, and compare each measurement with its sourced target under a stated workload and configuration. Choose only the categories relevant to the supplied feature; a category that does not apply is justified, not tested for completeness. No custom runner or other skill is required; use the project's own tools.

## Optional project guide

Before executing non-functional tests, look for `AIAugmentation/project_guides/execute-nonfunctional-tests-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, quality targets, workloads, tools, environments, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-execution boundaries.

## Inputs and scope

- Read the quality targets and non-functional scope from the test plan (A15), the risks (A06), the engineering and governance policies (E03) and the test baselines and workloads (E06), the prepared test resources (A18), repository and CI evidence (E05), environment records (E07) and any existing operational evidence (E08). Files, pasted text and existing project documents are acceptable. Preserve source IDs and versions where provided.
- Use only sourced targets, thresholds and workloads. When a requirement or policy calls for a quality attribute but no measurable target is supplied, measure only if the user asks, report the measurement without a pass or fail verdict, and record the missing target as a question. Do not invent thresholds.
- When non-functional testing is excluded from the baseline, record each relevant category as NOT APPLICABLE with the source of the exclusion, not as PASSED.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain non-functional scope and targets from A15, A06, E03 and E06, the workload and tools from E06 and A18, and the build and environment identity from E05 and E07. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`
- `A06_feasibility-assessment-outputs_{iteration_id}_v{artifact_version}.md`
- `E03_engineering-and-governance-policies_{iteration_id}_v{artifact_version}.md`
- `E06_test-and-defect-baselines_{iteration_id}_v{artifact_version}.md`
- `A18_test-resources-outputs_{iteration_id}_v{artifact_version}.md`
- `E05_repository-and-ci-evidence_{iteration_id}_v{artifact_version}.md`
- `E07_environment-and-access-records_{iteration_id}_v{artifact_version}.md`
- `E08_operational-and-product-evidence_{iteration_id}_v{artifact_version}.md`
- `A26_test-deployment-outputs_{iteration_id}_v{artifact_version}.md`

For revisions or re-runs, also read the supplied prior `A30_nonfunctional-testing-outputs_{iteration_id}_v{artifact_version}.md` and the changed build, configuration, workload or target that prompted the re-run.

## Authorization and execution boundary

- Run tests only when the user's request includes execution for the named build and environment. Otherwise, or when the environment cannot be reached, record results from supplied execution evidence, or plan the run and mark each case NOT RUN with the reason. Never present planned, designed or expected results as executed results.
- Use only the build, environment, accounts, data and commands identified by the user, the project instructions (for example their required checks or commands), the optional guide, A18 test resources, E05 repository and CI evidence or E07 environment records. Do not guess a command, endpoint or credential. If the identified command or environment is missing, ask for it and continue with work that does not depend on it.
- Stay within the test activity. Do not deploy or rebuild the application, change application code, test assets or environment configuration, close or file defects in an external tracker, or publish results externally. Do not run against production or with real personal data, secrets or shared resources unless the user explicitly authorizes that target and the project rules allow it; report the gap instead of working around it. Load, stress, soak, failover and security tests can disrupt shared systems or look like an attack: run them only against a target the user has explicitly authorized for that type of test, within the stated workload, time window and tool, and stop when the run threatens resources outside that scope.
- Record what actually ran: the command or procedure, the start and end time when available, the tool and version, and the exact native output location. Redact secrets and personal data from copied evidence and link the native file instead of pasting large output.

## Run the tests

1. **Pin the basis.** Record the exact `build_id`, `env_id`, environment size and configuration, and the source and version of every target. Note how the test environment differs from production when that affects how the results can be read.
2. **Select categories and targets.** For each relevant category (for example latency, throughput, capacity, reliability, security, accessibility or usability), state its source, the metric, the measurable target with units, and the requirement or risk it applies to. Justify each omitted or NOT APPLICABLE category.
3. **Define the workload and run configuration.** State the workload profile, data volume, concurrency, duration, ramp-up, warm-up and the tools and versions, using the sourced workload. Do not substitute an arbitrary workload when one is specified.
4. **Check readiness.** Confirm the target is authorized for this type of test, the environment is isolated or the shared-resource impact is accepted, and monitoring is in place. When a prerequisite is missing, mark the affected measurements BLOCKED with the obstacle.
5. **Execute or record.** Run the authorized tests, or import the supplied run, and capture raw measurements in their native format. Report the statistics the target is defined on (for example a percentile, mean or error rate) together with sample size, and keep warm-up and error samples identifiable.
6. **Compare and interpret.** Compare each measurement with its target and record the result. Record observations, anomalies and limitations, such as environment differences or short runs, that limit what the measurement shows. Recommend tuning or further investigation only as findings, not as changes you made.

Use these execution statuses for every in-scope measurement, and define them in the artifact:

- **PASSED:** executed, and every checked result matched the sourced target.
- **FAILED:** executed, and at least one actual result differed from the sourced target. Record the first failing step or checkpoint, the expected value and the actual value.
- **BLOCKED:** execution was attempted or due but could not complete because of a named obstacle, such as an unavailable environment, dependency, data, access or an unresolved question. Link the obstacle.
- **NOT RUN:** not attempted in this run, with the reason (for example out of the selected scope, not authorized or no designed case).

Only PASSED and FAILED count as executed. Keep BLOCKED and NOT RUN separate from executed results and from each other. A criterion without a designed measurement is a coverage gap, not a BLOCKED or NOT RUN result. Also use **NOT APPLICABLE** for a category that the scope excludes or that no requirement, policy or risk calls for, with the source of that decision. A measurement taken without a sourced target counts as executed but is reported as **MEASURED — NO TARGET**, never PASSED or FAILED.

For each FAILED measurement, raise a defect candidate with a stable ID (for example `DC-###`, or the existing defect ID when the defect is already registered in E06 or A34), the measurement ID, affected requirement and criterion IDs, build and environment, expected and actual results, reproduction steps and the evidence path. Propose a severity only when the project's defect taxonomy supplies one, and mark it as proposed. Triage, priority and assignment belong to `triage-defects` (A34); do not file the candidate in a defect tracker.

Before delivery, check that every measurement names its workload, tool, build, environment and target, no threshold or workload was invented, each omitted category is justified, and limitations that affect the interpretation are explicit.

## Output: A30 — Nonfunctional Testing Outputs

When working in this project, read and follow the [A30 template](../../../AIAugmentation/templates/A30_nonfunctional-testing-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A30_nonfunctional-testing-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Execution/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep native evidence in its original format and link it.

Include a short header with the feature, A30 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `scope`, `targets`, `measurements`, `build_id`, `env_id`, `workload`, `tools`, `limitations` and `findings`, referencing the child sections or native evidence rather than duplicating them. Then use these stable sections:

- **A30-01 — Measurements and comparison with quality targets:** One row per category and metric with the target and its source, the measured value with statistic, units and sample size, the result, and the native evidence path.
- **A30-02 — Run configuration, observations and limitations:** The workload profile, tools and versions, build, environment and configuration, run times, observations, anomalies and limitations, and the justification for each omitted or NOT APPLICABLE category.
- **A30-03 — Quality risks, findings and tuning recommendations:** Findings with stable IDs (for example `NFR-###`) linked to measurements and risks, defect candidates for FAILED measurements, and recommended investigations or tuning marked as recommendations. State explicitly when there are none.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native evidence files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A30-01 through A30-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` is not test-exit approval, and a measurement that meets its target in a test environment is not a production guarantee. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Preserve finding IDs and defect candidate IDs. A re-run with another build, configuration or workload is a new artifact version that keeps the earlier measurements visible, so trends can be compared. State what changed between runs; do not compare runs whose workloads or environments differ without saying so.

Finish with a link to A30, the result per category and the most important finding. A30 can be passed to `triage-defects` (A34) for failed targets, and to `report-test-progress` (A32) and `assess-test-readiness` (A33). Invoke those skills only when the user's scope includes that work. Do not automatically tune the system, change targets, re-run on a new build, declare test exit or publish results externally.

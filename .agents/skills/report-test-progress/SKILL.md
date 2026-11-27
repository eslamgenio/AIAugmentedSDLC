---
name: report-test-progress
description: DSK Report test execution progress from existing execution records for a stated reporting period and build scope, with planned and executed counts, defined status counts, coverage, defects, blockers, forecast risks and next actions. Produces the A32 test-progress bundle; does not execute tests, change results or approve test exit.
---

# Report test progress

Summarize where testing stands so a test lead and stakeholders can act on it. Every number must reconcile to the execution records it came from, and builds and reporting periods are never mixed silently. This skill reports; it does not run tests.

## Optional project guide

Before reporting progress, look for `AIAugmentation/project_guides/report-test-progress-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, status definitions, reporting periods, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-reporting boundaries.

## Inputs and scope

- Read the execution records for the reporting period (A27 smoke, A28 integration, A29 functional, A30 non-functional, A31 regression and A36 defect retest), the plan and its criteria (A15), the defect records and baselines (A34 and E06), the coverage review (A17) and the delivery milestones (E04). Files, pasted text and tool exports are acceptable. Preserve source IDs and versions where provided.
- If no execution records are supplied, ask for them. Report only what the records show: do not run tests, re-classify a result, or fill in a missing result.
- When records conflict, for example two statuses for the same test, build and run, flag the conflict and report both rather than choosing one.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain execution results from A27–A31 and A36, planned scope and criteria from A15, defect status from A34 and E06, coverage from A17, and milestones from E04. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A27_smoke-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A28_integration-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A29_functional-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A30_nonfunctional-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A31_regression-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A36_defect-retest-outputs_{iteration_id}_v{artifact_version}.md`
- `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`
- `A34_defect-triage-outputs_{iteration_id}_v{artifact_version}.md`
- `E06_test-and-defect-baselines_{iteration_id}_v{artifact_version}.md`
- `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md`
- `E04_delivery-planning-records_{iteration_id}_v{artifact_version}.md`

For revisions or re-runs, also read the supplied prior `A32_test-progress-outputs_{iteration_id}_v{artifact_version}.md` and the new or changed execution records for the next reporting period.

## Report the progress

1. **Pin the basis.** State the `reporting_period` with start and end, the build or builds in scope, and the exact execution record revisions used. Report each build separately; when you also give a combined view, say how repeated runs of the same test are counted.
2. **Define the counts.** Use the status definitions from the execution records (PASSED, FAILED, BLOCKED, NOT RUN and, for non-functional tests, NOT APPLICABLE) and define them in the report. Distinguish unique test IDs from executions, so three tests run on two builds are reported as three tests and six executions.
3. **Count and reconcile.** Give planned and executed counts and status counts per test level and build, taken from the records. Check that the counts add up: planned equals executed plus BLOCKED plus NOT RUN for each build. Show any difference and its cause rather than adjusting a number.
4. **Summarize coverage.** Report requirement and criterion coverage from execution results and from A17. Keep criteria without designed tests visible as coverage gaps, separate from blocked or not-run tests.
5. **Summarize defects and blockers.** Report defects by status from A34, A36 and E06, keeping a passed retest distinct from a closed defect. List each blocker with the affected tests, its owner when supplied, and what would remove it.
6. **Forecast and recommend.** Compare progress with the A15 schedule and the E04 milestones. Use only supplied dates and state the assumptions behind any forecast; when no date is supplied, say so rather than estimating one. Recommend next actions with an owner role, without starting them.

Before delivery, check that every count reconciles to the cited execution records, builds and periods are reported separately or their combination is explained, coverage gaps are not counted as results, defect and retest states are distinct, and no result, date or owner was invented.

## Output: A32 — Test Progress Outputs

When working in this project, read and follow the [A32 template](../../../AIAugmentation/templates/A32_test-progress-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A32_test-progress-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Execution/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep native evidence in its original format and link it.

Include a short header with the feature, A32 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `reporting_period`, `build_scope`, `planned_executed_counts`, `status_counts`, `defects`, `blockers` and `forecast`, referencing the child sections or native evidence rather than duplicating them. Then use these stable sections:

- **A32-01 — Test progress report with defined status counts:** The reporting period and build scope, status definitions, and planned, executed and status counts per test level and build with the reconciliation, each count linked to its source record.
- **A32-02 — Coverage, defect and blocker summary:** Requirement and criterion coverage with gaps, defects by status with retest and closure kept distinct, and blockers with the affected tests and what would remove them.
- **A32-03 — Forecast risks and recommended next actions:** Progress against the plan and supplied milestones, forecast risks with their assumptions, and recommended next actions with owner roles. State explicitly when no date or milestone is supplied.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native evidence files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A32-01 through A32-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` is not test-exit approval, and good progress is not a test-exit recommendation; that belongs to `assess-test-readiness` (A33). An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Each reporting period is a new artifact version; keep earlier reports unchanged so trends stay visible. Preserve blocker and risk IDs across periods and state which were resolved, which remain and which are new. When a source record is corrected after a report, issue a new version that names the correction.

Finish with a link to A32, the headline counts per build, the main blockers and the next actions. A32 can be passed to `assess-test-readiness` (A33) together with the execution records. Invoke it only when the user's scope includes the exit assessment. Do not automatically run tests, triage defects, declare test exit or publish the report externally.

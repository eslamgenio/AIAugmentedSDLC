---
name: assess-test-readiness
description: DSK Assess a test candidate build against the plan's exit criteria using execution, coverage, defect and progress evidence, with a criterion-by-criterion result, gaps, residual risks and a READY or NOT READY recommendation for the human test-exit gate. Produces the A33 test-exit assessment; does not execute tests, waive criteria or grant test-exit approval.
---

# Assess test readiness

Give the human test owner an evidence-based view of whether the exit criteria are met for a specific candidate build. Assess every criterion on its own evidence; the recommendation follows from those results, not the other way round. The decision to exit testing belongs to the human owner.

## Optional project guide

Before assessing readiness, look for `AIAugmentation/project_guides/assess-test-readiness-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, exit criteria, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-assessment boundaries.

## Inputs and scope

- Read the exit criteria from the test plan (A15), the human decisions and any recorded waivers (E09), the coverage review (A17), the execution records (A27–A31 and A36), the defect records and baselines (A34 and E06), the risks (A06) and the progress report (A32). Files, pasted text and tool exports are acceptable. Preserve source IDs and versions where provided.
- If the exit criteria or the candidate build are not identified, ask for them. When no A15 criteria exist, assess only against criteria the user or a policy supplies, and state that the plan's criteria were unavailable. Do not invent criteria or thresholds.
- Do not run tests to fill a gap. Missing evidence makes a criterion PENDING, not MET.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the exit criteria from A15, decisions and waivers from E09, execution evidence from A27–A31 and A36, coverage from A17, defects from A34 and E06, risks from A06, and progress from A32. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`
- `E09_human-decisions_{iteration_id}_v{artifact_version}.md`
- `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A27_smoke-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A28_integration-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A29_functional-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A30_nonfunctional-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A31_regression-testing-outputs_{iteration_id}_v{artifact_version}.md`
- `A34_defect-triage-outputs_{iteration_id}_v{artifact_version}.md`
- `A36_defect-retest-outputs_{iteration_id}_v{artifact_version}.md`
- `E06_test-and-defect-baselines_{iteration_id}_v{artifact_version}.md`
- `A06_feasibility-assessment-outputs_{iteration_id}_v{artifact_version}.md`
- `A32_test-progress-outputs_{iteration_id}_v{artifact_version}.md`

For revisions or re-runs, also read the supplied prior `A33_test-exit-assessment-outputs_{iteration_id}_v{artifact_version}.md` and the new evidence, candidate build or decision that prompted the reassessment.

## Assess the criteria

1. **Pin the candidate.** Record the `candidate_id` and its build ID, and the exact revisions of every evidence artifact used. Use only evidence produced on the candidate build, or state why evidence from another build still applies. Do not combine results across builds silently.
2. **List the criteria.** Take every exit criterion from A15 with its ID (for example `EX-###`) and its measurable condition. Include execution exit and any test-design exit criteria. Do not drop, merge or reword a criterion. If criteria lack IDs, assign local labels and show the source-text mapping. If the plan defines no execution exit criterion, record that as a gap with an open question for the test owner rather than treating test exit as unconstrained.
3. **Assess each criterion.** Give each one a result with its evidence: **MET** when the cited evidence satisfies the condition, **NOT MET** when the evidence shows it is not satisfied, or **PENDING** when evidence is missing, conflicting or produced on another build. Cite the artifact, ID, status or count behind each result. A waiver counts only when E09 records it from an authorized human owner; cite it and keep the underlying result visible.
4. **Identify gaps.** List unmet and pending criteria, coverage gaps, open defects by severity, blocked and not-run tests, and pending human decisions, each with what would close it.
5. **State residual risks.** Link the risks (A06) and gaps to their possible impact if testing exited now. Do not invent likelihood or impact ratings.
6. **Recommend.** Recommend **READY** only when every exit criterion is MET, or waived in E09 with the waiver cited, and no unresolved blocking defect or pending decision affects the criteria. Otherwise recommend **NOT READY** and name the criteria and actions that would change the result.

Before delivery, check that every A15 exit criterion is assessed with cited evidence, results use only the candidate build's evidence or explain the exception, waivers are cited from E09 rather than assumed, and the recommendation follows from the criterion results.

## Output: A33 — Test Exit Assessment Outputs

When working in this project, read and follow the [A33 template](../../../AIAugmentation/templates/A33_test-exit-assessment-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A33_test-exit-assessment-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.

Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Execution/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep native evidence in its original format and link it.

Include a short header with the feature, A33 version, source filenames/versions, scope and draft status. Fill the template's **Required content** table with the catalog fields `candidate_id`, `criterion_results`, `evidence_refs`, `gaps`, `residual_risks` and `recommendation`, referencing the child sections or native evidence rather than duplicating them. Then use these stable sections:

- **A33-01 — Criterion-by-criterion exit assessment:** One row per exit criterion with its ID, condition, result (MET, NOT MET or PENDING), the cited evidence and any recorded waiver.
- **A33-02 — Unmet criteria and residual risk summary:** The unmet and pending criteria, coverage gaps, open defects, blocked and not-run tests and pending decisions, with the residual risks they leave and what would close each one.
- **A33-03 — Recommendation and evidence for the human gate:** The READY or NOT READY recommendation, the reasons, the evidence package the human owner should review, and the decision that is needed and who holds it. State that this recommendation is not test-exit approval.

Summarize missing information, open decisions and limitations in **Acceptance and handoff**, and record the catalog acceptance check result with its evidence.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. List the native evidence files with their exact paths and checksums or revisions in `evidence_refs` when known. Preserve the template child registry A33-01 through A33-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` is distinct from the READY or NOT READY recommendation, and neither is human test-exit approval. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Preserve criterion IDs and gap IDs. A reassessment after new evidence, a new candidate build or a human decision is a new artifact version that keeps the earlier assessment unchanged. For each previously unmet or pending criterion, state whether it is now MET, still unmet or still pending, with the new evidence. A prior READY recommendation never carries over to a different candidate build.

Finish with a link to A33, the recommendation and the criteria that drive it. The human test owner uses A33 to make the test-exit decision and records it in E09. On NOT READY, the gaps can go to `triage-defects` (A34) or back to the relevant test design or execution skill; after a recorded human exit decision, A33 can go to `summarize-test-results` (A38). Invoke those skills only when the user's scope includes that work. Never record the human decision yourself, waive a criterion, declare test exit or start release activities.

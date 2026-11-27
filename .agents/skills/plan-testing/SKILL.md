---
name: plan-testing
description: DSK Create or revise a scoped, risk-based software test plan from a requirements baseline and acceptance criteria, with test levels, responsibilities, schedule, environment needs and measurable entry, exit and suspension criteria. Produces the A15 test-planning bundle consumed by test design; does not design cases, execute tests or approve test exit.
---

# Plan testing

Turn the user's reviewed requirements into a test plan that a test designer, a test lead and a reviewer can act on. Work across domains; choose levels, priorities and criteria appropriate to the supplied feature. Use the supplied requirements directly; no custom runner or other skill is required.

## Optional project guide

Before planning, look for `AIAugmentation/project_guides/plan-testing-guide.md` relative to the project root. If it exists, read it and apply its relevant project-specific conventions together with this skill. If it is absent, continue with the generic instructions here. The guide may specialize defaults such as source locations, domain rules, test levels, identifiers, checks and output conventions, but it does not override higher-priority instructions, the user's explicit request or this skill's authorization and test-planning boundaries.

## Inputs and scope

- Read the supplied requirements baseline and acceptance criteria, plus any relevant scope decisions, risks, design details, delivery plan, test policies, environment records or test template. Files, pasted text and existing project documents are acceptable. Preserve source IDs and versions where provided.
- For revisions, also read the prior test plan and the review findings, changed requirements or user feedback that prompted the revision.
- If the feature requirements are absent, ask for them. Otherwise start with the usable information. Missing formal approval, a risk register, a delivery plan or environment records does not prevent a clearly marked draft.
- Do not invent scope, risks, dates, people, environments, tools, coverage targets or quality thresholds. Record a targeted question or an explicit `Missing — impact / owner` entry when missing information changes the plan; continue planning unaffected areas. Distinguish source-backed plan content from suggested additional checks.
- If source statements lack IDs, assign local REQ/AC labels and show the source-text mapping. These labels organize existing statements; they do not create new requirements or acceptance criteria.

### Named input artifacts


Resolve explicit input paths first. For folder-based discovery, establish the active iteration root (not just a supplied phase subfolder), then search that root and its subfolders for the named inputs, including other phases and `External Inputs/`. Match artifact IDs and compatible versions, and record exact source paths. Do not select files from other iterations unless explicitly supplied or referenced by the baseline. If multiple candidates claim the same artifact/version or sources conflict, flag the ambiguity and resolve it before using the affected input; continue unaffected work. Reference original inputs instead of copying them between phases. Existing flat iteration folders remain supported.

In the selected input/iteration folder, read the following named artifacts when they exist. Obtain the requirements baseline from A05 and its embedded content or referenced baseline, together with A04 acceptance criteria and A02 scope boundaries. Also accept supplied requirements documents or text regardless of filename; no particular requirements filename is mandatory. If A05 embeds the complete behavior, context and scope, a separate requirements file is unnecessary. Follow an external baseline reference when needed to obtain missing content; ask only when essential behavior or scope is still missing or conflicting. Substitute the selected iteration and artifact version in each filename pattern; respect explicitly supplied versions and record the exact files used. When no version is specified, use the latest compatible artifact versions within the selected iteration, checking their baseline references rather than mixing snapshots silently. These are the project Markdown names; also accept a supplied equivalent format. Missing optional supporting artifacts do not prevent a useful draft under the rules above.

- `A05_requirements-review-outputs_{iteration_id}_v{artifact_version}.md`
- `A04_acceptance-criteria-outputs_{iteration_id}_v{artifact_version}.md`
- `A02_scope-definition-outputs_{iteration_id}_v{artifact_version}.md`
- `E09_human-decisions_{iteration_id}_v{artifact_version}.md`
- `A06_feasibility-assessment-outputs_{iteration_id}_v{artifact_version}.md`
- `A09_system-component-design-outputs_{iteration_id}_v{artifact_version}.md`
- `A14_iteration-planning-outputs_{iteration_id}_v{artifact_version}.md`
- `E04_delivery-planning-records_{iteration_id}_v{artifact_version}.md`
- `E06_test-and-defect-baselines_{iteration_id}_v{artifact_version}.md`
- `E03_engineering-and-governance-policies_{iteration_id}_v{artifact_version}.md`
- `E07_environment-and-access-records_{iteration_id}_v{artifact_version}.md`
- `E01_business-context_{iteration_id}_v{artifact_version}.md`

For revisions, also read the supplied prior `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md` and any review findings or changed source revisions that prompted it.

## Plan the testing

1. **Pin the basis.** Record the exact baseline, criteria and supporting revisions used. Note whether the A05 review gate is READY, REVISE or BLOCKED and whether human agreement is evidenced in E09. A non-READY gate or pending agreement does not stop a draft plan; carry it into the entry criteria and open decisions instead of treating the plan as approved.
2. **Define the scope.** Give the plan a stable `plan_id` (reuse an existing one on revision). List every in-scope requirement and acceptance criterion by ID, and every exclusion, deferral or undecided item with its source. Do not widen scope with untraced features or narrow it silently. Each in-scope requirement must appear in the plan, either as planned coverage or as an explicit blocked/open item.
3. **Prioritize by risk.** Link supplied risks (for example A06 `RISK-###`) to the affected requirements and state how each risk shapes emphasis: priority, depth, level or specific conditions to cover such as boundaries, state transitions, failure paths or integrations. When no risk register is supplied, identify candidate product risks from the requirements and mark them as proposed, not as an assessed register. Do not invent likelihood or impact ratings.
4. **Choose test levels and types.** For each level (for example component, integration, system, acceptance or non-functional), state what it covers, the requirement IDs it applies to and why it fits, using supplied design and interface details. Choose only levels and types relevant to the feature; avoid an unrelated test-category checklist. Name a non-functional type only when a requirement, policy or risk calls for it, and keep its measurement conditions and threshold as sourced.
5. **Assign responsibilities and schedule.** Identify the activities (test design, coverage review, revision, resource preparation, execution by others, exit decision) with the role responsible for each. Use supplied names, dates and milestones from A14, E04 or E09 only; otherwise record the role and sequence and mark the person or date as missing. The human test owner, not this skill, makes approval and exit decisions.
6. **State environment and data needs.** Describe the capabilities required to carry out the planned tests: setup, controllable inputs, observable outputs, accounts, fixtures or tools. Reference supplied environment records and mark unverified readiness explicitly. Do not claim that an environment exists or is ready.
7. **Write measurable criteria.** Give each entry, exit and suspension/resumption criterion a stable ID and a condition someone can check as met or not met, citing the artifact, ID, status or count it depends on. Separate test-design exit (for example every in-scope criterion accounted for in A16 and a READY A17 recommendation) from execution exit, which depends on results the plan does not produce. Use supplied coverage or defect thresholds only; when none is supplied, record the question rather than choosing a number.

Before delivery, check that every in-scope requirement and criterion is accounted for, every listed risk links to requirements or is marked unlinked with a reason, each criterion is measurable, environment needs and open decisions are explicit, and no date, person, threshold or approval was invented.

## Output: A15 — Test Planning Outputs

When working in this project, read and follow the [A15 template](../../../AIAugmentation/templates/A15_test-planning-outputs.md) before writing the output. Fill its applicable sections, replace placeholders, and retain stable child IDs. If the skill is copied elsewhere without the project templates, use the self-contained layout below. The repository template governs the canonical artifact.

Write one canonical, readable Markdown document, named `A15_test-planning-outputs_{iteration_id}_v1.0.md` for a first standalone draft. Substitute the source iteration ID; if none is available, start with `ITER-001`. Reuse supplied iteration/version conventions; increment the version for revisions and avoid replacing unrelated existing work. If file writing is unavailable, return the same content in the conversation.


Resolve the output folder in this order: an explicitly requested location; the prior version's folder when revising this artifact; a location configured by project instructions or the optional guide; otherwise the active `AIAugmentation/artifacts/<iteration_id>/` folder. When phase layout is configured without a specific output override, use `Test Preparation/` beneath the active iteration root for this artifact. Respect a configured artifact root, create only the needed output folder, and do not relocate earlier files. Write an actual, readable Markdown artifact using the canonical filename and extension. Preserve the artifact ID, exact input revisions, evidence links and version metadata; do not emit a JSON payload or parallel JSON manifest. Keep native evidence in its original format and link it.

Include a short header with the feature, A15 version, source filenames/versions or source-text mapping, scope and draft/review status. Fill the template's **Required content** table with the catalog fields `plan_id`, `scope`, `levels`, `risks`, `responsibilities`, `schedule` and `entry_exit_suspension_criteria`, referencing the child sections rather than duplicating them. Then use these stable sections:

- **A15-01 — Test strategy and scoped test plan:** plan ID and objective, in-scope requirement/criterion IDs, exclusions with sources, risk-to-requirement priorities and the test approach for each priority area.
- **A15-02 — Test levels, responsibilities and schedule:** levels and types with the requirement IDs they cover, activity/role/owner rows, sequence and any supplied dates or milestones, and environment and data needs with their readiness evidence.
- **A15-03 — Entry, exit and suspension criteria:** criteria with stable IDs (for example `EN-###`, `EX-###`, `SU-###`), the measurable condition, the evidence source and current status (Met / Not met / Pending) where known. Include resumption conditions for each suspension criterion.

Record open questions in the template's **Open questions** table with an ID, affected requirements or plan items, the decision or information needed and its planning impact, or state that there are none. Summarize missing information and open decisions in **Acceptance and handoff**.

Use YAML front matter with exactly these nine canonical keys: artifact_id, schema_version, artifact_version, producer_or_owner, iteration_id, created_at, source_artifact_versions, status, evidence_refs. Use null for unknown scalar metadata and empty lists for unavailable source/evidence references, with the reason in the body. Preserve the template child registry A15-01 through A15-03 with each version and an embedded anchor or relative path; use null for an unknown value and verify resolved references. Use the same contract in the standalone layout. The artifact `status` is not human approval of the plan. An incompatible requested format must not replace the canonical Markdown artifact; explain the mismatch.

## Revisions and handoff

Before delivery, verify that front matter parses, each required key appears once, version and iteration match the filename, and Markdown links within the output to project artifacts are relative and resolve from the output document's folder. Avoid machine-specific absolute paths for project files; disclose missing targets rather than inventing replacements.

Preserve all source/input files and prior output versions. Save each revision as a new file with an incremented artifact version in its filename and document header; never overwrite an existing source or prior version.

Preserve the `plan_id` and the IDs of unchanged criteria, risks and plan items. Assign new IDs to new items; record removed or superseded items without reusing their IDs. When a revision follows a changed baseline, list the affected requirements and plan items so downstream test cases and coverage can be rechecked. Include a short response for each review finding: changed, retained with explanation, or blocked pending clarification.

Finish with a link to A15 and a brief note about open decisions. It can be passed, together with the same requirements baseline, to `create-test-cases` to produce A16. Invoke that skill only when the user's scope includes test design. Do not automatically design cases, execute tests, approve the plan, declare test exit or publish to a test-management system.

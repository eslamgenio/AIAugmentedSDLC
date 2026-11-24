---
name: review-requirements
description: "Independently review a Requirements-phase scope, requirements and acceptance criteria before test design. Find material contradictions, missing business rules, gaps in observable acceptance evidence, and open decisions; report scoped READY, REVISE, or BLOCKED without rewriting source artifacts."
---

# Review Requirements

Produce a read-only Markdown review. Use this skill for initial review and closure against a revised Requirements packet. The default next consumer is test design; READY does not mean the implementation or its tests passed.

## Pin the packet

1. Record the supplied scope, requirements, criteria and applicable primary source artifacts by ID/path and exact revision (commit/hash/user-supplied immutable revision where available). Use the versions requested or explicitly designated authoritative, not whichever file is newest. If only unversioned text is supplied, label it as a snapshot and do not certify cross-revision closure. Identify inaccessible/missing evidence and assess unaffected portions.
2. Preserve existing requirement (`RQ-###`), acceptance criterion (`AC-###`), and source/question IDs verbatim. For clauses without IDs, use unmistakably local locators and a short evidence quote when needed. Do not mint upstream IDs or silently treat drafts, open questions, proposed criteria, or assumptions as approved.
3. Index in-scope requirements, exclusions/deferred items, and supplied criteria by links to requirement IDs. Review all in-scope items, not just requirements with existing criteria. Report orphaned/duplicate IDs and incompatible revisions when material. A coverage label is not evidence.

## Check the observable contract

For each in-scope behavior inspect the actor, preconditions, trigger, actionable input, authorized behavior, transitions/side effects, and observable result as applicable. Check applicable positive and negative paths, conditions and precedence, exceptional states, and meaningful missing assertions. Do not import an unrelated checklist.

- Compare each requirement with its source and each acceptance criterion with the requirement. No criterion may settle an unknown or override an authoritative exception by implication. Surface conflicting sources without choosing a rule unless authority or explicit precedence resolves it.
- Derive decision points from the specified rule independently of the supplied criteria. For thresholds, inspect the exact threshold and nearest representable input on each relevant side using the specified units and precision; for time, use the stated instant, zone and inclusivity. If two adjacent examples imply a boundary but do not assert the exact decision point, flag the gap. A table claiming “full coverage” does not remove the gap.
- Require controllable setup and an observable, source-backed expected result. A readily testable rule with a missing assertion is a revision; a critical expected result that cannot be determined because of unknown authority, conflicting evidence, or a missing business decision is blocked.
- Keep optional improvements separate. A finding must change a real implementation or testing decision. Use impact-based priorities (High/Medium/Low unless a scheme was supplied). Give the smallest corrective action or decision question, never an invented decision.

## Record and gate

For each materially affected requirement or group, show the `RQ`/criterion IDs, evidence, gaps and status. Overall status is the worst status within the requested review scope:

- **BLOCKED:** A required source or consequential decision is missing or conflicting and prevents determining an expected result or completing the relevant review. Name what would unblock it and what can proceed independently.
- **REVISE:** The evidence is adequate to establish intended behavior, but material clarification in wording, acceptance coverage, or observable assertions is missing. Name the correction and reassess the revised packet.
- **READY:** The scope/revisions are identified, the applicable expected outcomes are evidenced, and no material finding or decisive gap remains in the stated scope. Non-blocking suggestions do not change readiness. Do not use READY for unavailable evidence or assumptions.

Assign each finding a stable `RR-###` (use existing IDs where available); include status (`OPEN`, `CLOSED`, or `UNVERIFIED`), category, priority, affected IDs, evidence/precise gap, consequence, and next action. Keep an RR ID across wording changes if the underlying issue is the same; separate genuinely new findings and never recycle IDs.

## Verify closure

Read the previous review and the exact revised inputs. Verify every prior open RR against the revised evidence, including concrete expected outcomes at decisive examples; do not rely on a change summary or merely on a new criterion existing. Cite the exact revised source/criterion locator. Mark CLOSED only after the fix and its evidence are checked; otherwise carry OPEN, or mark UNVERIFIED where the relevant revised evidence is unavailable. If a prior review is missing, perform a fresh review rather than pretending continuity. Recompute scoped and overall gates and report relevant regressions.

Use the [review format and fixtures](references/review-format.md). Deliver the revision table, concise status and rationale, scoped readiness, findings, questions, and next handoff. Leave authoritative requirements, tracker records and criteria untouched; suggested edits are proposals. Do not claim to run tests from documentation review.

## DevSkillKit A05 handoff

Produce an actual Markdown file named `A05_requirements-review-outputs_{iteration_id}_v{artifact_version}.md` in the requested or established artifact location. If naming metadata or a writable target is unavailable, return the same Markdown inline as a draft and state the blocker; do not invent metadata or claim a save. Preserve earlier versions and the inputs.

Read and follow the existing repo-relative template `AIAugmentation/templates/A05_requirements-review-outputs.md` before writing canonical A05. Fill its actual sections, preserve the catalog field labels and child IDs, and remove unresolved placeholders by labelling the missing evidence explicitly. If the template is unavailable, return a clearly labelled draft instead of claiming compliance with the project template.

Start the file with YAML front matter between `---` delimiters. Include `artifact_id`, `schema_version`, `artifact_version`, `producer_or_owner`, `iteration_id`, `created_at`, `source_artifact_versions`, `status`, and `evidence_refs`. Use known values, exact source revisions and actual creation time when known. For drafts, use null for unknown scalars or empty lists for absent verified references where the schema permits. Use YAML sequences for `source_artifact_versions` and `evidence_refs`, including when empty. Artifact status is separate from readiness and human approval.

Use supplied A02/A03/A04 artifacts and applicable E01/E03/E04/E09 evidence. Explicitly supplied legacy inputs may be read; write new artifacts only as Markdown. Use the project template for named output sections and consult the [review format](references/review-format.md) for review guidance and synthetic examples. Preserve `## Child Artifact Register` with `Child ID | Version | Location` for A05-01, A05-02 and A05-03. For each embedded child, record this A05 parent version and a link to its exact retained heading anchor (`#a05-01`, `#a05-02`, or `#a05-03` respectively). For a separate child, record the child's exact supplied version and verified path relative to this artifact. Do not use the parent version for a separate child or assume a path; identify any unknown version or location explicitly. A proposed baseline remains proposed regardless of review readiness until authorized agreement is evidenced.

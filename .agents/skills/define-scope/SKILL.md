---
name: define-scope
description: Define or update the boundaries of a release, feature, or initiative from a brief or elicited requirements. Classify what is in, out, deferred, or undecided and record dependencies, tradeoffs, and approval evidence. Use when deciding what to include, not when eliciting needs or designing the solution.
---

# Define Scope

DevSkillKit activity **A02: Define scope and business goals**. Turn the available evidence into a boundary that a human can approve and that requirements analysis can use. A request for a scope proposal is not approval of that proposal.

## Work from the inputs

- Read the user's release target, goal, constraints, elicitation brief or equivalent, existing product boundaries, and any recorded scope decisions. In DevSkillKit, use available A01 and E01/E03/E04/E02 evidence; do not silently substitute unverified versions. Read an explicitly supplied legacy JSON artifact as an input only; do not rewrite it or emit JSON output. Separate budget, schedule, and policy constraints from assumptions. If the boundary (which release or initiative) is unclear, label a working interpretation and keep affected items provisional; ask only if the answer materially changes the scope.
- Preserve supplied requirement IDs, evidence/source IDs, open-question IDs, and exact artifact version or location when known. If an input has no IDs, use stable local references such as `RQ-001` and `SRC-001` with a pointer to the source; label inferred interpretations. Never reuse an ID for different content. Cite direct scope decision evidence separately from evidence that someone requested an item.
- Split partly included requirements into named slices only when the evidence supports the boundary. Keep the original RQ ID as the parent and give slices stable suffixes (for example, `RQ-004.a`, `RQ-004.b`). Classify the slices, not the unsplit parent; retain explicit exclusions and open questions.

## Draw the boundary

| Disposition | Meaning |
| --- | --- |
| In scope | Included or proposed for this specific release or initiative. Explicitly state which. |
| Out of scope | Explicitly excluded from this boundary. Do not infer permanent exclusion. |
| Deferred | Deliberately postponed. Include a revisit trigger or target only if known. |
| Undecided | Evidence is missing or contradictory, or a required decision has not been made. |

Give each item one disposition for the target. Label recommendations as proposals. Silence, an uncertain dependency, a stakeholder wish, or a priority label alone must not become a confirmed inclusion, exclusion, or deferral. Keep unresolved conflicting sources visible; identify the decision needed and the tradeoff. Use existing owner names only when supplied, otherwise mark owner TBD.

For each material dependency, record what is needed, which items it affects, and whether it is confirmed, assumed, unknown, or blocking. An included item can still have a blocking dependency. Do not imply that dependency work is included unless its own boundary is stated. Note missing thresholds or delivery commitments without inventing them.

## Return the scope statement and handoff

In the DevSkillKit artifact flow, read and follow the template at `AIAugmentation/templates/A02_scope-definition-outputs.md` relative to the repository root before writing. Preserve its headings and catalog fields; replace placeholders without inventing values. Write `A02_scope-definition-outputs_{iteration_id}_v{artifact_version}.md` to the requested or established artifact location. The file is a Markdown document, not a fenced payload. If required naming/version information is missing or no writable location is available, return a clearly labeled draft without inventing a version, claiming it was saved, or overwriting a baseline.

**YAML front matter.** Put these nine existing keys in the front matter of the output artifact: `artifact_id`, `schema_version`, `artifact_version`, `producer_or_owner`, `iteration_id`, `created_at`, `source_artifact_versions`, `status`, `evidence_refs`. Keep exact source revisions, evidence references, and verified project metadata. Use YAML null for unknown scalar values and empty lists when there are no verified source versions or evidence references only where the catalog permits; otherwise label the output an inline draft and name the missing data. Artifact `status` is not human approval or technical readiness.

Use the following Markdown sections, retaining the existing deliverable IDs:

1. **A02-01 — Scope statement.** Provide the stable Scope ID, release/initiative target, and a scope register. Use rows with `RQ ID | Parent RQ ID if split | Capability or boundary | Disposition | Decision state | Evidence/decision refs | Rationale or condition`. Keep In scope, Out of scope, Deferred, and Undecided discernible, whether as named subsections or in the disposition column. Do not treat deferred or undecided work as confirmed exclusions. List proposed and confirmed inclusions with their distinct decision states.
2. **A02-02 — Business goals and success measures.** Use `Goal | Metric | Target | Units or time window | Source or open decision`. Write "Not yet agreed" when no target is supported and link the open decision, rather than inventing a threshold. Do not turn a budget or delivery constraint into a success metric.
3. **A02-03 — Constraints, assumptions, and agreement checklist.** Separate evidenced budget, schedule, policy, and capability constraints from assumptions. Show dependencies with affected RQ IDs, status, and impact; show open decisions with question ID, owner if known, and the evidence or approval required. State Agreement status as `Draft`, `Pending approval`, or `Approved`, and record decision reference, approving role/person, and date when known. Approval must cover this exact scope; carry forward approval only for unchanged boundaries the evidence covers. Neither a checklist nor stakeholder silence constitutes approval.
4. **Handoff to requirements analysis.** Pass in-scope items with decision states, note which dependencies actually block analysis, and keep deferred, excluded, and unresolved items visible without converting them into acceptance criteria.

Under `## Child Artifact Register`, include the columns `Child ID | Version | Location` and one row each for A02-01, A02-02 and A02-03. For an embedded child, use the parent artifact's actual version and a link to that child's exact section anchor (`#a02-01`, `#a02-02`, or `#a02-03` in the template); preserve the anchor in the rendered file. For a verified separate child, use the child's own exact version and a relative link from the parent document to that file. Mark unknown versions or locations explicitly and do not infer provenance, mirror the parent version for a separate child, or add a guessed link. Check each populated link resolves to the intended child.

For a standalone request outside the catalog artifact flow, return this human-readable structure in Markdown without requiring catalog metadata.

Before returning, check that every candidate ID is classified or represented by classified slices; dispositions for the same slice and target do not conflict; and no proposal, assumption, or dependency was silently approved.

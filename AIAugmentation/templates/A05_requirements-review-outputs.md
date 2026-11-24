---
artifact_id: A05
schema_version: null
artifact_version: null
producer_or_owner: review-requirements
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A05 — Requirements Review Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **Feature / project:** [Name]
- **Scope:** [Included behavior, boundaries and exclusions]
- **Review gate:** [READY, REVISE, or BLOCKED with rationale; not stakeholder approval]
- **Output filename:** `A05_requirements-review-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `baseline_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `req_versions` | [Value, evidence or section reference; explicitly identify missing information] |
| `review_findings` | [Value, evidence or section reference; explicitly identify missing information] |
| `actions` | [Value, evidence or section reference; explicitly identify missing information] |
| `stakeholder_decision_refs` | [Value, evidence or section reference; explicitly identify missing information] |

## Child Artifact Register

Use the parent artifact version for embedded children and link the exact retained anchor. For a standalone child, record its exact supplied version and a verified path relative to this artifact. If either value is unknown, state which value is unknown; do not invent a target. Replace table guidance when producing the artifact.

| Child ID | Version | Location |
| --- | --- | --- |
| A05-01 | [Parent artifact version if embedded] | [Embedded](#a05-01) |
| A05-02 | [Parent artifact version if embedded] | [Embedded](#a05-02) |
| A05-03 | [Parent artifact version if embedded] | [Embedded](#a05-03) |

<a id="a05-01"></a>

## A05-01 — Requirements review findings and actions

[Provide the following: Requirements review findings and actions. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a05-02"></a>

## A05-02 — Proposed baseline with revision history

Include the complete requirements baseline here (goal, terminology, initial state, requirement IDs and behavior, acceptance criteria, scope and exclusions), or reference an accessible versioned baseline supplied for the task. A separate file with a particular name is not required. Preserve the baseline behavior version separately from this artifact version and record any changes.

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a05-03"></a>

## A05-03 — Agreement record with pending decisions

[Provide the following: Agreement record with pending decisions. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Baseline identifies reviewed revisions. Open decisions block claims of approval.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H016, H019, H023, H025, H029, H043, H046, H049

**If rejected or incomplete:** Return invalid or incomplete output to review-requirements. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

---
artifact_id: A01
schema_version: null
artifact_version: null
producer_or_owner: null
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A01 — Requirements Elicitation Outputs

> Template: fill YAML front matter using verified values, repeat list entries under source_artifact_versions and evidence_refs, replace placeholders, and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A01
- **artifact_name:** Requirements Elicitation Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** elicit-requirements
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A01_requirements-elicitation-outputs_{iteration_id}_v{artifact_version}.md`

## Discovery snapshot

[Goal, affected actors, current workflow, release context if known, and source limitations.]

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

### `needs` records

| `need_id` | `source` | `user` | `problem` | `owner` |
| --- | --- | --- | --- | --- |
| [NEED-###] | [SRC ID and exact locator] | [Actor] | [Problem] | [Accountable person or role, or Unassigned] |

### `requirements` records

| `req_id` | `scenario` | `status` | `need_ids` | `source_ids` | Constraints or uncertainty |
| --- | --- | --- | --- | --- | --- |
| [RQ-###] | [Actor and scenario] | [stated / inferred / disputed] | [Need IDs] | [Source IDs and locators] | [Exact stated qualifier or unresolved issue] |

### `questions` records

| `owner` | `status` | `question_id` | `question` | `req_ids` | `impact` |
| --- | --- | --- | --- | --- | --- |
| [Accountable person or role, or Unassigned] | [open / resolved] | [Q-###] | [Decision-shaped question] | [Affected RQ IDs] | [What this blocks or changes] |

## Child Artifact Register

| Child ID | Version | Location |
| --- | --- | --- |
| A01-01 | [Parent artifact_version if embedded; exact child version if separate; otherwise Unknown] | [#a01-01](#a01-01) |
| A01-02 | [Parent artifact_version if embedded; exact child version if separate; otherwise Unknown] | [#a01-02](#a01-02) |
| A01-03 | [Parent artifact_version if embedded; exact child version if separate; otherwise Unknown] | [#a01-03](#a01-03) |

> For a separate child, replace the embedded link with its exact path relative to this artifact. If its location is unverified, write `Unknown`. Do not infer child versions from filenames without evidence. Embedded entries point to the exact anchors below and inherit the explicit parent version.

<a id="a01-01"></a>

## A01-01 — Stakeholder needs register with source links

[Provide the following: Stakeholder needs register with source links. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a01-02"></a>

## A01-02 — Draft requirements and user scenarios

[Provide the following: Draft requirements and user scenarios. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a01-03"></a>

## A01-03 — Open questions and assumptions log

[Provide the following: Open questions and assumptions log. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

### Decisions

[Preserve decision IDs, authority, status, and exact source locators; otherwise None identified.]

### Assumptions

[Record unconfirmed assumptions separately with source links where known; otherwise None identified.]

## Acceptance and handoff

**Catalog acceptance checks:** Every need has evidence and an owner. Assumptions remain explicit.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H004, H007, H011, H022, H109

**If rejected or incomplete:** Return invalid or incomplete output to elicit-requirements. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

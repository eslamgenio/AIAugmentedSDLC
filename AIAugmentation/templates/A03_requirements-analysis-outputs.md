---
artifact_id: A03
schema_version: null
artifact_version: null
producer_or_owner: analyze-requirements
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A03 — Requirements Analysis Outputs

> Template: replace placeholders and remove guidance when creating an artifact. Populate YAML metadata with verified values, keeping source revisions and evidence references as arrays. See [template usage](README.md).

- **artifact_name:** Requirements Analysis Outputs
- **Feature / project:** [Name]
- **Prepared by / date:** [Actual author and date]
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A03_requirements-analysis-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `conflicts` | [Value, evidence or section reference; explicitly identify missing information] |
| `clarification_status` | [Value, evidence or section reference; explicitly identify missing information] |

### `requirements` records

| `req_id` | `priority` | `rationale` | `dependencies` |
| --- | --- | --- | --- |
| [req_id] | [priority] | [rationale] | [dependencies] |

## Child Artifact Register

| Child ID | Version | Location |
| --- | --- | --- |
| A03-01 | [Parent artifact version] | [Analyzed and prioritized requirements backlog](#a03-01) |
| A03-02 | [Parent artifact version] | [Conflict and clarification register](#a03-02) |
| A03-03 | [Parent artifact version] | [Priority rationale and dependency links](#a03-03) |

An embedded child uses the exact parent artifact version and its section anchor. For a separately saved child, record its exact version and a Markdown relative path from this artifact's directory. Use `Unknown` explicitly for unavailable version or location; do not invent one.

<a id="a03-01"></a>

## A03-01 — Analyzed and prioritized requirements backlog

[Provide the following: Analyzed and prioritized requirements backlog. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a03-02"></a>

## A03-02 — Conflict and clarification register

[Provide the following: Conflict and clarification register. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a03-03"></a>

## A03-03 — Priority rationale and dependency links

[Provide the following: Priority rationale and dependency links. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Requirement IDs are unique. Conflicts and priority reasons are explicit.

- **Acceptance-criteria eligibility:** [Confirmed, ready, in-scope RQ IDs with evidence; separately list held, proposed, deferred, and excluded RQ IDs and reasons]
- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H010, H013, H031, H040

**If rejected or incomplete:** Return invalid or incomplete output to analyze-requirements. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

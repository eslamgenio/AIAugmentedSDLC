# A11 — Work Breakdown Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A11
- **artifact_name:** Work Breakdown Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** decompose-work
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A11_work-breakdown-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `estimates_pending` | [Value, evidence or section reference; explicitly identify missing information] |

### `items` records

| `work_id` | `req_ids` | `ac_ids` | `tasks` | `dependencies` | `done_criteria` |
| --- | --- | --- | --- | --- | --- |
| [work_id] | [req_ids] | [ac_ids] | [tasks] | [dependencies] | [done_criteria] |

## A11-01 — Epics, stories and actionable task breakdown

[Provide the following: Epics, stories and actionable task breakdown. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A11-02 — Requirement-to-work-item links

[Provide the following: Requirement-to-work-item links. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A11-03 — Dependencies and completion criteria per item

[Provide the following: Dependencies and completion criteria per item. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Tasks are scoped and traceable. Completion criteria and dependencies are present.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H034, H037, H040, H058, H132

**If rejected or incomplete:** Return invalid or incomplete output to decompose-work. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

---
artifact_id: A15
schema_version: "1.0"
artifact_version: null
producer_or_owner: plan-testing
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A15 — Test Planning Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A15
- **artifact_name:** Test Planning Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** plan-testing
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A15_test-planning-outputs_{iteration_id}_v{artifact_version}.md`

## Child artifacts

| Child ID | Version | Embedded anchor or relative path |
| --- | --- | --- |
| A15-01 | null | #a15-01 |
| A15-02 | null | #a15-02 |
| A15-03 | null | #a15-03 |

Replace each known version; an embedded child can use the parent version when that version is confirmed. Use a relative path for a separately stored versioned Markdown child and verify that it resolves. Keep unknown versions or paths explicitly null; do not invent them. For native evidence, retain its format and link its exact path/revision or checksum.

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `plan_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `scope` | [Value, evidence or section reference; explicitly identify missing information] |
| `levels` | [Value, evidence or section reference; explicitly identify missing information] |
| `risks` | [Value, evidence or section reference; explicitly identify missing information] |
| `responsibilities` | [Value, evidence or section reference; explicitly identify missing information] |
| `schedule` | [Value, evidence or section reference; explicitly identify missing information] |
| `entry_exit_suspension_criteria` | [Value, evidence or section reference; explicitly identify missing information] |

<a id="a15-01"></a>

## A15-01 — Test strategy and scoped test plan

[Provide the following: Test strategy and scoped test plan. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a15-02"></a>

## A15-02 — Test levels, responsibilities and schedule

[Provide the following: Test levels, responsibilities and schedule. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a15-03"></a>

## A15-03 — Entry, exit and suspension criteria

[Provide the following: Entry, exit and suspension criteria. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

### Open questions

| Question ID | Affected requirement / plan item IDs | Decision or information needed | Planning impact |
| --- | --- | --- | --- |
| [Q-ID] | [IDs] | [Specific question and owner] | [Blocked item, assumption or None] |

State None when there are no open questions. This document records a test plan, not test design, executed results or human approval of the plan or of test exit.

## Acceptance and handoff

**Catalog acceptance checks:** Criteria are measurable. Required scope and environment needs are explicit.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H047, H088, H095, H097, H112

**If rejected or incomplete:** Return invalid or incomplete output to plan-testing. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

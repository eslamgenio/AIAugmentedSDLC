---
artifact_id: A29
schema_version: "1.0"
artifact_version: null
producer_or_owner: execute-functional-tests
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A29 — Functional Testing Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A29
- **artifact_name:** Functional Testing Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** execute-functional-tests
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A29_functional-testing-outputs_{iteration_id}_v{artifact_version}.md`

## Child artifacts

| Child ID | Version | Embedded anchor or relative path |
| --- | --- | --- |
| A29-01 | null | #a29-01 |
| A29-02 | null | #a29-02 |
| A29-03 | null | #a29-03 |

Replace each known version; an embedded child can use the parent version when that version is confirmed. Use a relative path for a separately stored versioned Markdown child and verify that it resolves. Keep unknown versions or paths explicitly null; do not invent them. For native evidence, retain its format and link its exact path/revision or checksum.

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `test_ids` | [Value, evidence or section reference; explicitly identify missing information] |
| `req_ids` | [Value, evidence or section reference; explicitly identify missing information] |
| `ac_ids` | [Value, evidence or section reference; explicitly identify missing information] |
| `build_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `env_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `actual` | [Value, evidence or section reference; explicitly identify missing information] |
| `expected` | [Value, evidence or section reference; explicitly identify missing information] |
| `status` | [Value, evidence or section reference; explicitly identify missing information] |
| `evidence` | [Value, evidence or section reference; explicitly identify missing information] |

<a id="a29-01"></a>

## A29-01 — Test execution records with actual results

[Provide the following: Test execution records with actual results. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a29-02"></a>

## A29-02 — Requirement-linked evidence and failure details

[Provide the following: Requirement-linked evidence and failure details. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a29-03"></a>

## A29-03 — Defect candidates and blocked-test reasons

[Provide the following: Defect candidates and blocked-test reasons. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

This document records executed functional results against an identified build and environment. Blocked and not-run cases stay separate from executed cases; defect candidates are not triaged defects or human approval.

## Acceptance and handoff

**Catalog acceptance checks:** Every executed case has actual results. Blocked and not-run cases remain separate.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If rejected or incomplete:** Return invalid or incomplete output to execute-functional-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

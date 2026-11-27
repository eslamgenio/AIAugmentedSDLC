---
artifact_id: A31
schema_version: "1.0"
artifact_version: null
producer_or_owner: execute-regression-tests
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A31 — Regression Testing Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A31
- **artifact_name:** Regression Testing Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** execute-regression-tests
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A31_regression-testing-outputs_{iteration_id}_v{artifact_version}.md`

## Child artifacts

| Child ID | Version | Embedded anchor or relative path |
| --- | --- | --- |
| A31-01 | null | #a31-01 |
| A31-02 | null | #a31-02 |
| A31-03 | null | #a31-03 |

Replace each known version; an embedded child can use the parent version when that version is confirmed. Use a relative path for a separately stored versioned Markdown child and verify that it resolves. Keep unknown versions or paths explicitly null; do not invent them. For native evidence, retain its format and link its exact path/revision or checksum.

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `suite_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `selected_test_ids` | [Value, evidence or section reference; explicitly identify missing information] |
| `impact_rationale` | [Value, evidence or section reference; explicitly identify missing information] |
| `build_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `results` | [Value, evidence or section reference; explicitly identify missing information] |
| `exclusions` | [Value, evidence or section reference; explicitly identify missing information] |
| `residual_risks` | [Value, evidence or section reference; explicitly identify missing information] |

<a id="a31-01"></a>

## A31-01 — Selected regression scope and selection rationale

[Provide the following: Selected regression scope and selection rationale. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a31-02"></a>

## A31-02 — Regression results with evidence and build ID

[Provide the following: Regression results with evidence and build ID. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a31-03"></a>

## A31-03 — New failures, excluded coverage and residual risks

[Provide the following: New failures, excluded coverage and residual risks. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

This document records the selected regression scope and its executed results against an identified build. Excluded coverage stays visible as residual risk; results are not human approval or test exit.

## Acceptance and handoff

**Catalog acceptance checks:** Selection traces to changes and coverage. Exclusions are explicit.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If rejected or incomplete:** Return invalid or incomplete output to execute-regression-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

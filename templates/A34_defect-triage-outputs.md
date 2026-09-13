# A34 — Defect Triage Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A34
- **artifact_name:** Defect Triage Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** triage-defects
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A34_defect-triage-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `duplicates` | [Value, evidence or section reference; explicitly identify missing information] |
| `severity` | [Value, evidence or section reference; explicitly identify missing information] |
| `owner_proposals` | [Value, evidence or section reference; explicitly identify missing information] |

### `defects` records

| `defect_id` | `req_id` | `build_id` | `env_id` | `steps` | `expected` | `actual` | `evidence` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [defect_id] | [req_id] | [build_id] | [env_id] | [steps] | [expected] | [actual] | [evidence] |

## A34-01 — Structured defect report drafts

[Provide the following: Structured defect report drafts. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A34-02 — Duplicate analysis and proposed classification

[Provide the following: Duplicate analysis and proposed classification. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A34-03 — Triage notes, owner suggestions and next actions

[Provide the following: Triage notes, owner suggestions and next actions. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Defects are reproducible. Proposed ownership and priority need triage confirmation.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H064, H095, H098, H103, H106, H108, H113, H134

**If rejected or incomplete:** Return invalid or incomplete output to triage-defects. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

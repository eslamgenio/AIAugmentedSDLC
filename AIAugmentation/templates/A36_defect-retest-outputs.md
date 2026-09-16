# A36 — Defect Retest Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A36
- **artifact_name:** Defect Retest Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** retest-defects
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A36_defect-retest-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `defect_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `corrected_build_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `original_evidence_ref` | [Value, evidence or section reference; explicitly identify missing information] |
| `retest_steps` | [Value, evidence or section reference; explicitly identify missing information] |
| `result` | [Value, evidence or section reference; explicitly identify missing information] |
| `evidence` | [Value, evidence or section reference; explicitly identify missing information] |
| `recommendation` | [Value, evidence or section reference; explicitly identify missing information] |

## A36-01 — Retest execution result and evidence

[Provide the following: Retest execution result and evidence. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A36-02 — Fix verification linked to defect and build

[Provide the following: Fix verification linked to defect and build. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A36-03 — Closure or reopening recommendation

[Provide the following: Closure or reopening recommendation. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Retest uses the corrected build. Closure is only a recommendation until owner confirmation.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If rejected or incomplete:** Return invalid or incomplete output to retest-defects. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

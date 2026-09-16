# A25 — CI Validation Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A25
- **artifact_name:** CI Validation Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** validate-ci-checks
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A25_ci-validation-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `pipeline_run_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `code_revision` | [Value, evidence or section reference; explicitly identify missing information] |
| `artifact_digest` | [Value, evidence or section reference; explicitly identify missing information] |
| `required_jobs` | [Value, evidence or section reference; explicitly identify missing information] |
| `statuses` | [Value, evidence or section reference; explicitly identify missing information] |
| `evidence` | [Value, evidence or section reference; explicitly identify missing information] |
| `reruns` | [Value, evidence or section reference; explicitly identify missing information] |

## A25-01 — CI check status summary with evidence links

[Provide the following: CI check status summary with evidence links. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A25-02 — Missing, failed or skipped job analysis

[Provide the following: Missing, failed or skipped job analysis. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A25-03 — Remediation or rerun recommendations

[Provide the following: Remediation or rerun recommendations. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** No missing or skipped mandatory job is treated as passing. Revision and artifact match.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H076

**If rejected or incomplete:** Return invalid or incomplete output to validate-ci-checks. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

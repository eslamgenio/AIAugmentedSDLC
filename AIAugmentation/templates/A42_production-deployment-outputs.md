# A42 — Production Deployment Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A42
- **artifact_name:** Production Deployment Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** deploy-release
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A42_production-deployment-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `candidate_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `artifact_digest` | [Value, evidence or section reference; explicitly identify missing information] |
| `active_version` | [Value, evidence or section reference; explicitly identify missing information] |
| `env_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `approval_ref` | [Value, evidence or section reference; explicitly identify missing information] |
| `checkpoints` | [Value, evidence or section reference; explicitly identify missing information] |
| `outcome` | [Value, evidence or section reference; explicitly identify missing information] |
| `rollback_state` | [Value, evidence or section reference; explicitly identify missing information] |

## A42-01 — Production deployment record and active version

[Provide the following: Production deployment record and active version. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A42-02 — Checkpoint results and deployment evidence

[Provide the following: Checkpoint results and deployment evidence. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A42-03 — Completion, failure or rollback outcome report

[Provide the following: Completion, failure or rollback outcome report. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Deployment matches approved candidate and scope. Failure or rollback is reported explicitly.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H080, H101, H128

**If rejected or incomplete:** Return invalid or incomplete output to deploy-release. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

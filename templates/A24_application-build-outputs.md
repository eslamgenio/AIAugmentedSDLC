# A24 — Application Build Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A24
- **artifact_name:** Application Build Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** build-application
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A24_application-build-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `artifact_uri` | [Value, evidence or section reference; explicitly identify missing information] |
| `version` | [Value, evidence or section reference; explicitly identify missing information] |
| `digest` | [Value, evidence or section reference; explicitly identify missing information] |
| `source_commit` | [Value, evidence or section reference; explicitly identify missing information] |
| `build_log` | [Value, evidence or section reference; explicitly identify missing information] |
| `dependency_manifest` | [Value, evidence or section reference; explicitly identify missing information] |
| `provenance` | [Value, evidence or section reference; explicitly identify missing information] |

## A24-01 — Versioned application package or container image

[Provide the following: Versioned application package or container image. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A24-02 — Build log and artifact checksums

[Provide the following: Build log and artifact checksums. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## A24-03 — Dependency manifest and build provenance

[Provide the following: Dependency manifest and build provenance. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

## Acceptance and handoff

**Catalog acceptance checks:** Package exists and its digest, version and source revision are traceable.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H074, H076, H112, H115, H118, H125

**If rejected or incomplete:** Return invalid or incomplete output to build-application. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

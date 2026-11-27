---
artifact_id: A30
schema_version: "1.0"
artifact_version: null
producer_or_owner: execute-nonfunctional-tests
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A30 — Nonfunctional Testing Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A30
- **artifact_name:** Nonfunctional Testing Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** execute-nonfunctional-tests
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A30_nonfunctional-testing-outputs_{iteration_id}_v{artifact_version}.md`

## Child artifacts

| Child ID | Version | Embedded anchor or relative path |
| --- | --- | --- |
| A30-01 | null | #a30-01 |
| A30-02 | null | #a30-02 |
| A30-03 | null | #a30-03 |

Replace each known version; an embedded child can use the parent version when that version is confirmed. Use a relative path for a separately stored versioned Markdown child and verify that it resolves. Keep unknown versions or paths explicitly null; do not invent them. For native evidence, retain its format and link its exact path/revision or checksum.

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Required content

Keep these catalog fields identifiable. Values may reference a detailed child section or a native deliverable below instead of duplicating it. Repeat record rows as needed.

| Field | Value or section reference |
| --- | --- |
| `scope` | [Value, evidence or section reference; explicitly identify missing information] |
| `targets` | [Value, evidence or section reference; explicitly identify missing information] |
| `measurements` | [Value, evidence or section reference; explicitly identify missing information] |
| `build_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `env_id` | [Value, evidence or section reference; explicitly identify missing information] |
| `workload` | [Value, evidence or section reference; explicitly identify missing information] |
| `tools` | [Value, evidence or section reference; explicitly identify missing information] |
| `limitations` | [Value, evidence or section reference; explicitly identify missing information] |
| `findings` | [Value, evidence or section reference; explicitly identify missing information] |

<a id="a30-01"></a>

## A30-01 — Measurements and comparison with quality targets

[Provide the following: Measurements and comparison with quality targets. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a30-02"></a>

## A30-02 — Run configuration, observations and limitations

[Provide the following: Run configuration, observations and limitations. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

<a id="a30-03"></a>

## A30-03 — Quality risks, findings and tuning recommendations

[Provide the following: Quality risks, findings and tuning recommendations. Use the required fields above; link their detailed values here instead of duplicating them.]

| Deliverable item | Content or native file reference | Supporting source / revision | Open issue / limitation |
| --- | --- | --- | --- |
| [Stable item ID or name] | [Specific content or resolvable file] | [Evidence and version] | [Issue or None] |

This document records non-functional measurements against sourced targets and an identified workload, build and environment. An unmeasured category is NOT RUN or NOT APPLICABLE with a reason, never PASSED; findings are not human approval.

## Acceptance and handoff

**Catalog acceptance checks:** Measurements identify workloads and thresholds. Omitted categories are justified.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H094, H098, H100, H113

**If rejected or incomplete:** Return invalid or incomplete output to execute-nonfunctional-tests. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

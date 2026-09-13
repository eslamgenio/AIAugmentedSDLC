# A16 — Test Case Creation Outputs

> Template: replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A16
- **artifact_name:** Test Case Creation Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** create-test-cases
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A16_test-case-creation-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## A16-01 — Requirement-linked test cases and scenarios

Repeat this block for each case. Preserve IDs during revisions. Use supplied source IDs; otherwise document the mapping from local labels to source text.

### [test_id] — [Title]

- **req_ids:** [Requirement IDs and source section]
- **ac_ids:** [Criterion IDs; Not supplied if absent]
- **suite_type:** [Functional / integration / regression / smoke / other relevant scope]
- **Test type:** [Positive / negative / boundary / other]
- **Status:** [READY FOR REVIEW / BLOCKED]
- **preconditions:** [Required state, roles, accounts and setup]
- **data:** [Concrete values, fixtures and relevant boundaries]
- **Question references:** [Blocking question IDs or None]

| Step | Action | Observable expected result and source |
| --- | --- | --- |
| 1 | [Specific action] | [Source-supported outcome; mark unresolved behavior BLOCKED] |

**expected:** [Final observable result and source; reference a step when sufficient]

## A16-02 — Preconditions, data needs and expected results

Summarize setup and data by test ID. Reference A16-01 expectations instead of maintaining a second copy.

| Test ID | Setup / environment capabilities | Data / fixtures | Expected result reference |
| --- | --- | --- | --- |
| [test_id] | [Required setup] | [Data reference] | [A16-01 case and step] |

## A16-03 — Coverage questions and automation candidates

### Questions

| Question ID | Requirement / criterion IDs | Affected tests | Missing behavior / question | Owner | Blocking impact | Status / decision reference |
| --- | --- | --- | --- | --- | --- | --- |
| [Q-ID] | [IDs] | [IDs or Not yet designed] | [Targeted question] | [Owner or Unassigned] | [Why it affects expectations] | [OPEN or supported decision] |

### Automation candidates

| Test ID | Candidate? | Reason | Setup or observability constraints |
| --- | --- | --- | --- |
| [test_id] | [Yes / No / Pending] | [Repeatability and observable outcome] | [Constraints] |

### Scope accounting

| Requirement / criterion ID | Test IDs | Coverage or exclusion | Reason / question reference |
| --- | --- | --- | --- |
| [ID] | [IDs or None] | [Covered / Partial / Blocked / Out of scope] | [Source-based explanation] |

### Responses to prior review findings

Use for revisions; otherwise state Not applicable — initial draft.

| Finding ID | Response | Affected test IDs | Change or reason | Remaining question |
| --- | --- | --- | --- | --- |
| [Existing finding ID] | [Changed / Retained with explanation / Blocked] | [IDs] | [Revision details] | [Question or None] |

Cases above constitute the catalog `cases` records; the Questions and Automation candidates sections supply `questions` and `automation_candidates`. This document records test design, not executed results or independently verified closure.

## Acceptance and handoff

**Catalog acceptance checks:** Cases have unique IDs and expected results. Suite type identifies smoke, integration, functional, regression or other scope.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H049, H052, H055, H079, H082, H085, H091, H101, H108

**If rejected or incomplete:** Return invalid or incomplete output to create-test-cases. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

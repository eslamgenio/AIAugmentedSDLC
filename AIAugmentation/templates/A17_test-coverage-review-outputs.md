---
artifact_id: A17
schema_version: null
artifact_version: null
producer_or_owner: review-test-coverage
iteration_id: null
created_at: null
source_artifact_versions: []
status: DRAFT
evidence_refs: []
---

# A17 — Test Coverage Review Outputs

> Template: retain the YAML keys and fill verified values. Quote exact version strings and use arrays for source version pins and evidence links, including the inspected A16 version/path when known. Keep unknowns as `null` or `[]` only where allowed; otherwise leave the artifact a draft. Replace placeholders and remove guidance when creating an artifact. See [template usage](README.md).

- **artifact_id:** A17
- **artifact_name:** Test Coverage Review Outputs
- **iteration_id:** [ITER-xxx]
- **artifact_version:** [1.0]
- **Feature / project:** [Name]
- **Producer / owner:** review-test-coverage
- **Prepared by / date:** [Actual author and date]
- **Document status:** DRAFT
- **Scope:** [Included behavior, boundaries and exclusions]
- **Output filename:** `A17_test-coverage-review-outputs_{iteration_id}_v{artifact_version}.md`

## Source references

| Source artifact / document | Exact filename or URI | Version / revision | Relevant section / evidence |
| --- | --- | --- | --- |
| [ID or source name] | [Resolvable reference] | [Version or identified snapshot] | [Section or evidence] |

## Review basis and recommendation

- **Candidate:** [Exact A16 filename and version, or supplied test snapshot]
- **baseline_refs:** [Exact requirements / acceptance criteria versions]
- **Recommendation:** [READY / REVISE / BLOCKED — choose after review]
- **Rationale:** [Evidence supporting the recommendation]
- **Limitations:** [Missing optional inputs, excluded scope and effects]

READY requires adequate scope coverage without blocking design defects or unresolved expected behavior. REVISE means corrections can use existing requirements. BLOCKED means an essential ambiguity or missing input requires an owner decision. READY does not grant human approval or imply tests passed.

## Child Artifact Register

For an embedded child, substitute the actual parent `artifact_version` and use its section anchor. For a separate child, specify its actual version and exact relative file path. Mark unknown versions or locations explicitly; do not infer them.

| Child ID | Version | Location |
| --- | --- | --- |
| A17-01 | [Parent version] | [Embedded section](#a17-01) |
| A17-02 | [Parent version] | [Embedded section](#a17-02) |
| A17-03 | [Parent version] | [Embedded section](#a17-03) |

<a id="a17-01"></a>

## A17-01 — Requirements-to-tests traceability matrix

Use one row per criterion, or requirement when criteria are absent. Inspect actual steps and expectations, not just declared links. Account for every baseline item.

| req_id | Criterion ID | Source behavior / location | test_ids | Coverage | Evidence and explanation |
| --- | --- | --- | --- | --- | --- |
| [REQ-ID] | [AC-ID or Not supplied] | [Required behavior] | [IDs or None] | [FULL / PARTIAL / NONE / BLOCKED / NOT APPLICABLE] | [Case/step evidence; justify exclusions] |

These rows provide the catalog `links` records. FULL requires coverage of all applicable behavior, including applicable criteria.

<a id="a17-02"></a>

## A17-02 — Coverage gap and duplicate case report

### Gaps

| Gap ID | Requirement / criterion | Missing scenario | Impact | Finding reference |
| --- | --- | --- | --- | --- |
| [GAP-ID] | [Source ID and location] | [Uncovered behavior] | [Why it matters] | [Finding ID] |

### Duplicates

| Duplicate group ID | Test IDs | Evidence of equivalent behavior | Distinct coverage to preserve | Finding reference |
| --- | --- | --- | --- | --- |
| [DUP-ID] | [Existing IDs] | [Matching setup, actions and outcomes] | [Differences or None] | [Finding ID] |

State None explicitly when no gaps or duplicates are found.

<a id="a17-03"></a>

## A17-03 — Test review findings and revision actions

### Findings

Repeat the block for each substantive finding. Preserve finding IDs on re-review.

#### [Finding ID] — [Title]

- **Severity:** [BLOCKING / NONBLOCKING]
- **Affected requirement / criterion IDs:** [IDs]
- **Affected test IDs:** [Existing IDs or Missing test]
- **Evidence:** [Exact source/candidate location or short excerpt]
- **Impact:** [Why the design is inadequate or could improve]
- **Requested correction:** [Concrete action supported by requirements]
- **Action owner:** [Creator / business decision owner / other]
- **Disposition:** [OPEN / RESOLVED / BLOCKED, with evidence]

### Revision actions

| Finding ID | Required action | Owner | Dependency / question | Status |
| --- | --- | --- | --- | --- |
| [Finding ID] | [Action] | [Owner or Unassigned] | [Reference or None] | [Status] |

### Verification of prior findings

Use on re-review; otherwise state Not applicable — initial review. Verify actual revised cases before closing a finding.

| Prior finding ID | Creator response | Inspected candidate / case / step | Verification result | Evidence / remaining action |
| --- | --- | --- | --- | --- |
| [Existing ID] | [Response] | [Exact reference] | [RESOLVED / UNRESOLVED / BLOCKED] | [Evidence] |

These sections supply `gaps`, `duplicates`, `findings` and `revision_actions`. Report other findings even when the overall recommendation is BLOCKED.

## Acceptance and handoff

**Catalog acceptance checks:** All baseline requirements are accounted for, including explicit uncovered items.

- **Check result and evidence:** [Assessed result, with evidence; Pending if not checked]
- **Missing information / open decisions:** [Specific gap, impact and owner; or None]
- **Next consumer / action:** [Applicable consumer and exact artifact version to hand off]

**Catalog handoff lookup:** Consumer and exact input are listed in these handoff rows: H055, H079, H082, H085, H091, H096, H098, H113

**If rejected or incomplete:** Return invalid or incomplete output to review-test-coverage. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change | Prior version / finding references |
| --- | --- | --- | --- |
| [Version] | [Date] | [Initial draft or actual changes] | [References or Not applicable] |

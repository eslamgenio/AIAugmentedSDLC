# A34 — Defect Triage Outputs

- **artifact_id:** A34
- **artifact_name:** Defect Triage Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** triage-defects
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A34_defect-triage-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A29 — Functional Testing Outputs](A29_functional-testing-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E06 — Test and Defect Baselines](E06_test-and-defect-baselines_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `defects[{defect_id,req_id,build_id,env_id,steps,expected,actual,evidence}]` | DEF-001: req_id=REQ-003; build_id=B001; env_id=LOCAL-TEST; steps=M,M,M,H,M,M,M for DEVICE-A; expected=2 notifications; actual=1; evidence=[native/B001_results.json](native/B001_results.json) TC-003 checkpoint 7 |
| `duplicates` | No duplicate in the supplied one-defect register; external register unavailable |
| `severity` | Proposed HIGH; misses a later offline incident |
| `owner_proposals` | Engineering owner unassigned; triage confirmation pending |

## A34-01 — Structured defect report drafts

DEF-001 is reproducible with the TC-003 sequence against SRC-001; reset state before reproducing.

## A34-02 — Duplicate analysis and proposed classification

Classify as notification lifecycle / state-reset defect. Proposed severity is HIGH, not an owner-approved priority.

## A34-03 — Triage notes, owner suggestions and next actions

Assign an engineer, review the proposed correction and retest the exact corrected build before closure.

## Acceptance and handoff

**Acceptance checks:** Defects are reproducible. Proposed ownership and priority need triage confirmation.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H064, H095, H098, H103, H106, H108, H113, H134

**If incomplete:** Return invalid or incomplete output to triage-defects. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

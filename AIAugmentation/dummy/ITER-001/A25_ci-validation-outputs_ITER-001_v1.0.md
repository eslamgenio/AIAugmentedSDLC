# A25 — CI Validation Outputs

- **artifact_id:** A25
- **artifact_name:** CI Validation Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** validate-ci-checks
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A25_ci-validation-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A21 — Code Validation Outputs](A21_code-validation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A24 — Application Build Outputs](A24_application-build-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E05 — Repository and CI Evidence](E05_repository-and-ci-evidence_ITER-001_v1.0.md), artifact version 1.0.
- [E03 — Engineering and Governance Policies](E03_engineering-and-governance-policies_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `pipeline_run_id` | LOCAL-RUN-001; no hosted CI run |
| `code_revision` | SRC-001 |
| `artifact_digest` | sha256:3ac9e676a0a3d158c14b6335db55f7fd78c7353730acb8a6d98d9be57dcd2bad |
| `required_jobs` | component cases; static analysis; code review |
| `statuses` | Component FAILED; static analysis NOT RUN; code review OPEN |
| `evidence` | [native/B001_results.json](native/B001_results.json); A21; A22 |
| `reruns` | Run corrected revision and obtain missing checks |

## A25-01 — CI check status summary with evidence links

Local evidence cannot be relabeled as successful hosted CI. The required-check summary is NOT READY.

## A25-02 — Missing, failed or skipped job analysis

TC-003 failed; static analysis is absent; CR-001 is open.

## A25-03 — Remediation or rerun recommendations

Re-run after correction and keep build/revision evidence aligned. A green subset cannot satisfy all mandatory jobs.

## Acceptance and handoff

**Acceptance checks:** No missing or skipped mandatory job is treated as passing. Revision and artifact match.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H076

**If incomplete:** Return invalid or incomplete output to validate-ci-checks. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

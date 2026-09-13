# A26 — Test Deployment Outputs

- **artifact_id:** A26
- **artifact_name:** Test Deployment Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** deploy-test-build
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A26_test-deployment-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A24 — Application Build Outputs](A24_application-build-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [A25 — CI Validation Outputs](A25_ci-validation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E07 — Environment and Access Records](E07_environment-and-access-records_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `build_id` | B001 |
| `artifact_digest` | sha256:3ac9e676a0a3d158c14b6335db55f7fd78c7353730acb8a6d98d9be57dcd2bad |
| `source_revision` | SRC-001 |
| `env_id` | LOCAL-TEST |
| `config_version` | LOCAL-CONFIG-1 |
| `deployment_log` | No managed deployment; local component invocation recorded by [native/B001_results.json](native/B001_results.json) |
| `health` | Local test execution available; service health not assessed |
| `rebuild_evidence` | B002 rebuild recorded in [native/build-records.json](native/build-records.json) for the later correction; not B001 validation |

## A26-01 — Rebuild evidence when needed and deployed build ID

B001 is available for isolated defect reproduction; A25 blocks advancement to a shared test environment.

## A26-02 — Deployment log and environment version record

LOCAL-TEST identifies an in-process harness with no endpoint or deployment account.

## A26-03 — Post-deployment status or recovery actions

Managed deployment status is BLOCKED. Later B002 evidence must not be used to declare B001 validated.

## Acceptance and handoff

**Acceptance checks:** Deployment uses a validated build. Corrected source must be rebuilt and pass checks before deployment.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H080, H083, H086, H093, H101, H107, H110

**If incomplete:** Return invalid or incomplete output to deploy-test-build. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

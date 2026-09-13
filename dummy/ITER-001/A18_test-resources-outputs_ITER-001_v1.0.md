# A18 — Test Resources Outputs

- **artifact_id:** A18
- **artifact_name:** Test Resources Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** prepare-test-resources
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A18_test-resources-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A16 — Test Case Creation Outputs](A16_test-case-creation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E06 — Test and Defect Baselines](E06_test-and-defect-baselines_ITER-001_v1.0.md), artifact version 1.0.
- [E07 — Environment and Access Records](E07_environment-and-access-records_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `dataset_refs` | [native/test_scenarios.json](native/test_scenarios.json) |
| `env_id` | LOCAL-TEST |
| `config_version` | LOCAL-CONFIG-1 |
| `setup_refs` | [native/run_cases.py](native/run_cases.py); initialize a new Monitor per case and register DEVICE-A |
| `readiness` | Local runner available; no shared environment or account provisioned |
| `cleanup_steps` | Discard Monitor instance between cases; preserve checked-in fixture files |

## A18-01 — Synthetic or masked test datasets

Dataset contains the event sequences for TC-001–003, with expected status and notification counts. Device IDs are DEVICE-A only; multi-device coverage remains absent.

## A18-02 — Environment setup scripts or configuration checklist

Python standard library only. Run the local runner from this folder with SRC-001 or SRC-002.

## A18-03 — Resource readiness record and cleanup procedure

Each case gets isolated in-memory state. No network endpoint, real account or persistent cleanup is required.

## Acceptance and handoff

**Acceptance checks:** Data is permitted and representative. Environment readiness has evidence.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H057, H081, H084, H087, H089, H093, H108, H110

**If incomplete:** Return invalid or incomplete output to prepare-test-resources. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

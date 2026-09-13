# A24 — Application Build Outputs

- **artifact_id:** A24
- **artifact_name:** Application Build Outputs
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** build-application
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `A24_application-build-outputs_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- [A20 — Feature Implementation Outputs](A20_feature-implementation-outputs_ITER-001_v1.0.md), artifact version 1.0.
- [E05 — Repository and CI Evidence](E05_repository-and-ci-evidence_ITER-001_v1.0.md), artifact version 1.0.

## Required content

| Field | Value / evidence |
| --- | --- |
| `artifact_uri` | [native/B001.zip](native/B001.zip) |
| `version` | B001 / 1.0.0-candidate.1 |
| `digest` | sha256:3ac9e676a0a3d158c14b6335db55f7fd78c7353730acb8a6d98d9be57dcd2bad |
| `source_commit` | SRC-001 content snapshot; not a Git commit |
| `build_log` | [native/build-records.json](native/build-records.json) |
| `dependency_manifest` | Python standard library; no third-party packages |
| `provenance` | Source archive containing monitor.py from SRC-001; build metadata in [native/build-records.json](native/build-records.json) |

## A24-01 — Versioned application package or container image

B001.zip is a local source package for the test candidate, not a production-certified build.

## A24-02 — Build log and artifact checksums

Verify the SHA-256 against [native/build-records.json](native/build-records.json) before consuming the package.

## A24-03 — Dependency manifest and build provenance

No dependency lockfile is required for this standard-library example; interpreter version is recorded separately.

## Acceptance and handoff

**Acceptance checks:** Package exists and its digest, version and source revision are traceable.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H074, H076, H112, H115, H118, H125

**If incomplete:** Return invalid or incomplete output to build-application. Retain the prior version and regenerate or correct the affected evidence. Failed test findings are valid evidence for triage, not permission to advance.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

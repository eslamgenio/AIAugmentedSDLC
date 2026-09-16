# E05 — Repository and CI Evidence

- **artifact_id:** E05
- **artifact_name:** Repository and CI Evidence
- **iteration_id:** ITER-001
- **artifact_version:** 1.0
- **Feature / project:** DEVICE-CONNECTION
- **Producer / owner:** Repository and CI/tool owners
- **Prepared by / date:** Codex / 2026-09-13
- **Document status:** DRAFT
- **Scope:** requirements.md v1.0; additional proposals are identified separately
- **Output filename:** `E05_repository-and-ci-evidence_ITER-001_v1.0.md`

## Source references

- [requirements.md](requirements.md), feature version 1.0.
- Owner/context record is supplied directly in this artifact; no external owner decision is inferred.

## Required content

| Field | Value / evidence |
| --- | --- |
| `repo_ref` | native/ source snapshots, no remote repository for the sample component |
| `revision` | SRC-001 and corrected SRC-002; content IDs rather than Git SHAs |
| `branch` | Not applicable; snapshots are files |
| `lockfiles` | None; standard library only |
| `tool_versions` | [native/runtime.txt](native/runtime.txt) |
| `commands` | python [native/run_cases.py](native/run_cases.py) SRC-001; python [native/run_cases.py](native/run_cases.py) SRC-002 |
| `pipeline_id` | No hosted CI configured |
| `run_id` | LOCAL-RUN-001 and LOCAL-RUN-002 |
| `check_results` | [native/B001_results.json](native/B001_results.json); [native/B002_results.json](native/B002_results.json); static checks absent |

## Supporting records

Repository evidence is the local source and runner. Hosted CI, remote branches and signed commits are not provided.

## Acceptance and handoff

**Acceptance checks:** Configuration and actual run evidence match the target revision. A configured check is not a completed check.

Use the recorded statuses and evidence above. Missing checks, reviews, owner agreement and deployment prerequisites remain outstanding; an artifact being present does not satisfy its gate.

**Consumer lookup:** Consumer and exact input are listed in these handoff rows: H056, H057, H059, H060, H062, H063, H067, H068, H071, H072, H073, H074, H075, H077, H084, H089, H104, H116

**If incomplete:** Request correction or a current record from Repository and CI/tool owners. Keep dependent work blocked until the required evidence or permission is supplied.

## Revision history

| Version | Date | Change |
| --- | --- | --- |
| 1.0 | 2026-09-13 | Initial record for this iteration. |

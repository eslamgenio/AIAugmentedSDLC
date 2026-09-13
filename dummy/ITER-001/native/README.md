# Component assets

`monitor_SRC-001.py` retains notification eligibility across recovery; `monitor_SRC-002.py` resets it. SRC-001 and SRC-002 identify file snapshots, not Git commits. B001 and B002 are source ZIP packages; their hashes and provenance are in [build-records.json](build-records.json).

From this directory, with Python installed:

```text
python run_cases.py SRC-001
python run_cases.py SRC-002
```

The first command returns exit code 1 with TC-003 failing; the second returns 0 with three passing cases. [test_scenarios.json](test_scenarios.json) supplies the checkpoint data. Results are written to standard output. Existing B001/B002 result files preserve the recorded runs.

This adapter implements the logical event interface for local use; it is not an accepted HTTP API. It has no network access, persistence or third-party dependencies. The runner covers TC-001–003 only; it does not cover the missing multi-device scenarios. Production integration, hosted CI and approvals are absent.

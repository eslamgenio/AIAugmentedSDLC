import json, sys
from pathlib import Path
base = Path(__file__).parent
revision = sys.argv[1] if len(sys.argv) > 1 else "SRC-002"
if revision not in ("SRC-001", "SRC-002"):
    raise SystemExit("Choose SRC-001 or SRC-002")
namespace = {}
exec(compile((base / ("monitor_" + revision + ".py")).read_text(), revision, "exec"), namespace)
records = []
for test_id, sequence in json.loads((base / "test_scenarios.json").read_text()).items():
    monitor = namespace["Monitor"]()
    monitor.register("DEVICE-A")
    checkpoints = []
    for number, (event, expected_status, expected_count) in enumerate(sequence, 1):
        status = monitor.process("DEVICE-A", {"M": "HEARTBEAT_MISSED", "H": "HEARTBEAT_RECEIVED"}[event]) if event else monitor.states["DEVICE-A"]["status"]
        passed = status == expected_status and len(monitor.notifications) == expected_count and all(x == "DEVICE-A" for x in monitor.notifications)
        checkpoints.append(dict(checkpoint=number,event=event or "INITIAL",expected_status=expected_status,actual_status=status,expected_notifications=expected_count,actual_notifications=len(monitor.notifications),status="PASSED" if passed else "FAILED"))
    records.append(dict(test_id=test_id,status="PASSED" if all(c["status"]=="PASSED" for c in checkpoints) else "FAILED",checkpoints=checkpoints))
print(json.dumps(dict(code_revision=revision,build_id="B001" if revision=="SRC-001" else "B002",env_id="LOCAL-TEST",records=records),indent=2))
sys.exit(1 if any(r["status"]=="FAILED" for r in records) else 0)

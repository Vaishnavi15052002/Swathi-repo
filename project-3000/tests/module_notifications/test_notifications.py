import pytest
from utils.recorder import TestRecorder
from utils.notifications import push

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        kind = "queue_full"
    elif i % 6 == 3:
        kind = "timeout"
    elif i % 6 == 1:
        kind = "invalid"
    else:
        kind = "normal"

    CASES.append({
        "tc_id": f"TC_NOTIF_{i:04}",
        "name": f"test_notifications_{i:04}",
        "module": "module_notifications",
        "file": "tests/module_notifications/test_notifications.py",
        "kind": kind
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_notifications(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Trigger notification")
    recorder.step("Step 2: Send notification")

    push(data["kind"])

import pytest
from utils.recorder import TestRecorder
from utils.subscriptions import renew

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        plan = "expired"
    elif i % 6 == 3:
        plan = "locked"
    elif i % 6 == 1:
        plan = "invalid"
    else:
        plan = "normal"

    CASES.append({
        "tc_id": f"TC_SUB_{i:04}",
        "name": f"test_subscriptions_{i:04}",
        "module": "module_subscriptions",
        "file": "tests/module_subscriptions/test_subscriptions.py",
        "plan": plan
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_subscriptions(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open subscriptions")
    recorder.step("Step 2: Renew plan")

    renew(data["plan"])

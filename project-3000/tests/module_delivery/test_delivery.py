import pytest
from utils.recorder import TestRecorder
from utils.delivery import ship

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        mode = "address_missing"
    elif i % 6 == 3:
        mode = "timeout"
    elif i % 6 == 1:
        mode = "blocked"
    else:
        mode = "normal"

    CASES.append({
        "tc_id": f"TC_DEL_{i:04}",
        "name": f"test_delivery_{i:04}",
        "module": "module_delivery",
        "file": "tests/module_delivery/test_delivery.py",
        "mode": mode
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_delivery(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Create delivery order")
    recorder.step("Step 2: Ship package")

    ship(data["mode"])

import pytest
from utils.recorder import TestRecorder
from utils.checkout import checkout

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        mode = "upi_fail"
    elif i % 6 == 3:
        mode = "card_timeout"
    elif i % 6 == 1:
        mode = "fraud"
    else:
        mode = "normal"

    CASES.append({
        "tc_id": f"TC_PAY_{i:04}",
        "name": f"test_checkout_{i:04}",
        "module": "module_checkout",
        "file": "tests/module_checkout/test_checkout.py",
        "mode": mode
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_checkout(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open checkout page")
    recorder.step("Step 2: Perform payment")

    checkout(data["mode"])

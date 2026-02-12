import pytest
from utils.recorder import TestRecorder
from utils.account import update_account

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        flag = "unauthorized"
    elif i % 6 == 3:
        flag = "conflict"
    elif i % 6 == 1:
        flag = "invalid"
    else:
        flag = "normal"

    CASES.append({
        "tc_id": f"TC_ACC_{i:04}",
        "name": f"test_account_{i:04}",
        "module": "module_account",
        "file": "tests/module_account/test_account.py",
        "flag": flag
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_account(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open profile page")
    recorder.step("Step 2: Update profile")

    update_account(data["flag"])

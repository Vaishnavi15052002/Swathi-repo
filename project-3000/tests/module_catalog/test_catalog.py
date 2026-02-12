import pytest
from utils.recorder import TestRecorder
from utils.catalog import load_catalog

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        kind = "empty"
    elif i % 6 == 3:
        kind = "corrupt"
    elif i % 6 == 1:
        kind = "slow"
    else:
        kind = "normal"

    CASES.append({
        "tc_id": f"TC_CAT_{i:04}",
        "name": f"test_catalog_{i:04}",
        "module": "module_catalog",
        "file": "tests/module_catalog/test_catalog.py",
        "kind": kind
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_catalog(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open catalog")
    recorder.step("Step 2: Load items")

    load_catalog(data["kind"])

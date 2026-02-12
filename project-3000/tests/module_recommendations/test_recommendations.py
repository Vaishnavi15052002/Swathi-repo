import pytest
from utils.recorder import TestRecorder
from utils.recommendations import recommend

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        mode = "model_fail"
    elif i % 6 == 3:
        mode = "no_data"
    elif i % 6 == 1:
        mode = "slow"
    else:
        mode = "normal"

    CASES.append({
        "tc_id": f"TC_REC_{i:04}",
        "name": f"test_reco_{i:04}",
        "module": "module_recommendations",
        "file": "tests/module_recommendations/test_recommendations.py",
        "mode": mode
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_recommendations(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open homepage")
    recorder.step("Step 2: Load recommendations")

    recommend(data["mode"])

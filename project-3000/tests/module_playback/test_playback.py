import pytest
from utils.recorder import TestRecorder
from utils.playback import play

CASES = []
for i in range(1, 401):
    if i % 6 == 0:
        video = "drm"
    elif i % 6 == 3:
        video = "region"
    elif i % 6 == 1:
        video = "slow"
    else:
        video = "normal"

    CASES.append({
        "tc_id": f"TC_PLAY_{i:04}",
        "name": f"test_playback_{i:04}",
        "module": "module_playback",
        "file": "tests/module_playback/test_playback.py",
        "video": video
    })


@pytest.mark.parametrize("data", CASES, ids=[c["tc_id"] for c in CASES])
def test_playback(request, data):
    recorder = TestRecorder(data["tc_id"], data["name"], data["module"], data["file"])
    request.node.test_recorder = recorder

    recorder.step("Step 1: Open video")
    recorder.step("Step 2: Start playback")

    play(data["video"])

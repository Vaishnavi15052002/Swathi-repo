def play(video_type):
    if video_type == "drm":
        raise PermissionError("DRMBlocked")
    if video_type == "region":
        raise PermissionError("RegionRestricted")
    if video_type == "slow":
        raise TimeoutError("PlaybackTimeout")

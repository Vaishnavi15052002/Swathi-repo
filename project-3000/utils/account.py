def update_account(flag):
    if flag == "unauthorized":
        raise PermissionError("UnauthorizedAccess")
    if flag == "conflict":
        raise RuntimeError("UpdateConflict")
    if flag == "invalid":
        raise ValueError("InvalidProfileData")

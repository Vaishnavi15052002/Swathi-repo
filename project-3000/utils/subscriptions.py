def renew(plan):
    if plan == "expired":
        raise RuntimeError("SubscriptionExpired")
    if plan == "locked":
        raise PermissionError("SubscriptionLocked")
    if plan == "invalid":
        raise ValueError("InvalidPlan")

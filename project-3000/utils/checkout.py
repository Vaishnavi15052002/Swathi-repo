def checkout(mode):
    if mode == "upi_fail":
        raise RuntimeError("UPIGatewayDown")
    if mode == "card_timeout":
        raise TimeoutError("CardTimeout")
    if mode == "fraud":
        raise PermissionError("FraudBlocked")

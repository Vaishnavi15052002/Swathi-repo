def ship(mode):
    if mode == "address_missing":
        raise KeyError("AddressMissing")
    if mode == "timeout":
        raise TimeoutError("DeliveryTimeout")
    if mode == "blocked":
        raise PermissionError("CarrierBlocked")

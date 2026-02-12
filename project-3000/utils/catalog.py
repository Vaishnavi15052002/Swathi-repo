def load_catalog(kind):
    if kind == "empty":
        raise LookupError("CatalogEmpty")
    if kind == "corrupt":
        raise ValueError("CatalogCorrupted")
    if kind == "slow":
        raise TimeoutError("CatalogLoadTimeout")

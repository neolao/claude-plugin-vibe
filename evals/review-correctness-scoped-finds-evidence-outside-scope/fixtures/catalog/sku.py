"""SKU handling; every module that keys on a SKU goes through normalize_sku."""


def normalize_sku(raw):
    """Canonical form of a SKU as typed by a human or read from a file:
    upper case, no surrounding blanks."""
    return raw.upper()

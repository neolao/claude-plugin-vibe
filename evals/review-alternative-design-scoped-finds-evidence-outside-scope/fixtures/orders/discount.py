def compute_discount_cents(subtotal_cents, kind, value):
    """Called at checkout for every order carrying a promo code."""
    if kind == "percentage":
        return subtotal_cents * value // 100
    elif kind == "fixed":
        return min(value, subtotal_cents)
    elif kind == "bogo":
        return subtotal_cents // 2
    raise ValueError(f"unknown discount kind: {kind}")

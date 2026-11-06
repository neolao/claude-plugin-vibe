def validate_discount(kind, value):
    """Called by the admin form that creates a promo code."""
    if kind == "percentage":
        return 0 < value <= 100
    elif kind == "fixed":
        return value > 0
    elif kind == "bogo":
        return value == 0
    raise ValueError(f"unknown discount kind: {kind}")

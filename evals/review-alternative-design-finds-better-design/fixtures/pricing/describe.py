def describe_discount(kind, value):
    """Label shown on the cart and on the invoice line."""
    if kind == "percentage":
        return f"{value}% off"
    elif kind == "fixed":
        return f"{value / 100:.2f} off"
    elif kind == "bogo":
        return "buy one get one"
    raise ValueError(f"unknown discount kind: {kind}")

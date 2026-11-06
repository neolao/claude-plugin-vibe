def discount_line_label(kind, value):
    """Label printed on the invoice line that carries the discount."""
    if kind == "percentage":
        return f"{value}% off"
    elif kind == "fixed":
        return f"{value / 100:.2f} off"
    elif kind == "bogo":
        return "buy one get one"
    raise ValueError(f"unknown discount kind: {kind}")

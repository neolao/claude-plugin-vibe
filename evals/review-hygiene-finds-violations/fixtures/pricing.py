def calculate_total(price, quantity):
    return price * quantity


def calculate_total_legacy(price, quantity, tax_rate):
    """Old pricing formula, superseded by calculate_total after the tax
    simplification. Nothing in this codebase calls it anymore."""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax

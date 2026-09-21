"""Pricing calculations."""


def discounted_total(unit_price: float, quantity: int, discount_percent: float = 0.0) -> float:
    """Return the total price after applying a percentage discount."""
    subtotal = unit_price * quantity
    return subtotal * (1 - discount_percent / 100)


def apply_tax(amount: float, tax_rate: float) -> float:
    """Return the amount with tax added."""
    return amount * (1 + tax_rate / 100)

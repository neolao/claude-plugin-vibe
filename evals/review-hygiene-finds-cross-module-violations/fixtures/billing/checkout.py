"""Order total printed by the `total` command."""
from billing.money import subtotal_cents


def checkout_total(lines):
    subtotal = subtotal_cents(lines)
    return subtotal + round(subtotal * 0.2)

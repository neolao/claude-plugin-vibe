"""Cent conversion of every amount shown or invoiced; see .vibe/decisions/001."""
from decimal import ROUND_DOWN, Decimal

CENT = Decimal("0.01")


def to_cents(amount):
    """Amount in euros (float from the provider) -> integer cents."""
    return int(Decimal(str(amount)).quantize(CENT, rounding=ROUND_DOWN) * 100)


def line_total_cents(unit_price, qty):
    return to_cents(unit_price) * qty

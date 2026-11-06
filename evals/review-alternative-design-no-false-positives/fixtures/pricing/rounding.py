from decimal import ROUND_HALF_UP, Decimal


def round_to_cents(amount):
    """Rounds a decimal amount of money to whole cents, half up, as the invoice shows it."""
    cents = (Decimal(amount) * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    return int(cents)

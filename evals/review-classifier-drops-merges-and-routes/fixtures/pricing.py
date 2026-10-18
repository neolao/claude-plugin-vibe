"""Order pricing. Called from the checkout flow once per order."""

LOYALTY_THRESHOLD = 500  # spend in cents over the last year


def loyalty_rate(spent_last_year):
    """Discount rate for a returning customer. The threshold is included."""
    if spent_last_year > LOYALTY_THRESHOLD:
        return 0.10
    return 0.0


def apply_discount(total, rate):
    if total is None:
        return None
    return round(total * (1 - rate), 2)


def price_order(order):
    rate = loyalty_rate(order.get("spent_last_year", 0))
    return apply_discount(order["total"], rate)

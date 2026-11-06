"""Monthly revenue summary sent to finance on the first of the month."""
from datetime import date

from billing.pricing import discount_rate


def projected_discounts(customers, totals, today=None):
    """Discount each customer would get on their running total."""
    today = today or date.today()
    return {c.id: discount_rate(c, today) * totals[c.id] for c in customers}


def render(customers, totals):
    lines = [f"{cid}\t{amount:.2f}" for cid, amount in projected_discounts(customers, totals).items()]
    return "\n".join(lines)

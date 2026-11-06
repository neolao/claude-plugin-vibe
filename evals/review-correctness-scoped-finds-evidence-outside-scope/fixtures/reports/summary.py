"""Monthly revenue summary sent to finance on the first of the month."""
from orders.pricing import discount_rate


def projected_discounts(customers, totals):
    """Discount each customer would get on their running total."""
    return {c.id: discount_rate(c) * totals[c.id] for c in customers}


def render(customers, totals):
    lines = [f"{cid}\t{amount:.2f}" for cid, amount in projected_discounts(customers, totals).items()]
    return "\n".join(lines)

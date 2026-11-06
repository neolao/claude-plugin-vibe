"""Monthly revenue summary sent to finance on the first of the month."""
from datetime import date

from orders.pricing import discount_rate
from reports.periods import months_in


def projected_discounts(customers, totals, today=None):
    """Discount each customer would get on their running total."""
    today = today or date.today()
    return {c.id: discount_rate(c, today) * totals[c.id] for c in customers}


def quarter_label(first_month):
    months = months_in(first_month, first_month + 2)
    return f"{months[0]:02d}-{months[-1]:02d}"


def render(customers, totals, first_month):
    lines = [f"{cid}\t{amount:.2f}" for cid, amount in projected_discounts(customers, totals).items()]
    return quarter_label(first_month) + "\n" + "\n".join(lines)

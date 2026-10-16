"""Order totals as the checkout page shows them."""

from orders.promotions import discount_for


def total_cents(order):
    gross = sum(line.unit_cents * line.quantity for line in order.lines)
    return gross - discount_for(order)


def total_label(order):
    return f"{total_cents(order) / 100:.2f} EUR"

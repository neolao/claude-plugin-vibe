# Called by the checkout page when the customer's loyalty card is scanned.
from orders.order import Order


def apply_loyalty_discount(order: Order, percent: int) -> None:
    order.apply_discount(percent)

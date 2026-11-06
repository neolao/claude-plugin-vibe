"""Checkout; called from the HTTP handlers in app/server.py."""
from datetime import date

from orders.pricing import discount_rate
from shipping.quotes import quote_for


def checkout_total(order, customer):
    """Amount charged at checkout: discounted subtotal plus shipping."""
    rate = discount_rate(customer, date.today())
    quote = quote_for(order.address)
    return order.subtotal * (1 - rate) + quote.amount

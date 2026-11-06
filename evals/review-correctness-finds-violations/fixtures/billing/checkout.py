"""Checkout; called from the HTTP handlers."""
from datetime import date

from billing.pricing import discount_rate


def checkout_total(customer, subtotal):
    rate = discount_rate(customer, date.today())
    return subtotal * (1 - rate)

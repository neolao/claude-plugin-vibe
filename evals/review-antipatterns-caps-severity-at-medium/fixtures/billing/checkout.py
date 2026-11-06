"""Checkout flow."""

from billing.tax import TaxCalculator


def charge(order, rates_source):
    calculator = TaxCalculator(rates_source)
    calculator.load_rates()
    return calculator.total(order.amount_cents, order.country)

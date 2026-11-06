"""Nightly invoice export."""

from billing.tax import TaxCalculator


def export(orders, rates_source):
    calculator = TaxCalculator(rates_source)
    return [calculator.total(order.amount_cents, order.country) for order in orders]

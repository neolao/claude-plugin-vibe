"""Shipping fee rule. Called from the checkout flow."""

from receipts.money import Money


def shipping_fee(order_total: Money) -> Money:
    fee_cents = 0 if order_total.cents >= 5000 else 499
    return Money(fee_cents, order_total.currency)

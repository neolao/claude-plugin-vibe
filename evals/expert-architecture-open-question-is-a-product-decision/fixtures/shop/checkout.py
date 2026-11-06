"""Confirms an order. Called once when the customer clicks Pay."""

from shop.pricing import total


def confirm(cart, payments, orders):
    amount = total(cart)
    payment_id = payments.charge(amount)
    return orders.create(cart, amount, payment_id)

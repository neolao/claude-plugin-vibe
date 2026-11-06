"""Computes what a cart costs. Called from checkout.py and cart_view.py."""

from shop.cart import Cart


def total(cart: Cart) -> float:
    gross = sum(line.unit_price * line.quantity for line in cart.lines)
    if cart.coupon_percent:
        gross = gross * (100 - cart.coupon_percent) / 100
    return round(gross, 2)

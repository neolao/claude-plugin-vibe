"""Coupon application at checkout. Called by the cart when a customer enters a code."""

from datetime import date

from audit import record


class CouponError(Exception):
    pass


def apply_coupon(cart, coupon, today=None):
    today = today or date.today()
    if coupon["expires"] < today:
        record("coupon_refused", code=coupon["code"])
        raise CouponError("Coupon expired")
    cart["total"] = round(cart["total"] * (1 - coupon["discount"]), 2)
    return cart

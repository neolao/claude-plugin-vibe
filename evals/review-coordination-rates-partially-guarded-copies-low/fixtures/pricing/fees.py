"""Shipping fee of a cart; called from the checkout flow."""

FREE_SHIPPING_THRESHOLD = 50.0
STANDARD_FEE = 4.9


def shipping_fee(cart_total):
    if cart_total >= FREE_SHIPPING_THRESHOLD:
        return 0.0
    return STANDARD_FEE

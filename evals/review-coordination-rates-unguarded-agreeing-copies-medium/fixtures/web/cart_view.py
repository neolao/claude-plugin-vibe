"""Cart page: shows the shipping banner above the item list."""
from pricing.fees import shipping_fee


def shipping_banner(cart_total):
    # keep in sync with pricing/fees.py
    if cart_total >= 50.0:
        return "Free shipping on this order"
    missing = 50.0 - cart_total
    return f"Add {missing:.2f} EUR for free shipping"


def render_cart(cart):
    total = sum(item.price * item.quantity for item in cart.items)
    return {
        "banner": shipping_banner(total),
        "fee": shipping_fee(total),
        "items": [item.as_row() for item in cart.items],
    }

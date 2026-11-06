"""Cart page: shows the shipping banner above the item list."""
from pricing.fees import FREE_SHIPPING_THRESHOLD, shipping_fee


def shipping_banner(cart_total):
    if cart_total >= FREE_SHIPPING_THRESHOLD:
        return "Free shipping on this order"
    missing = FREE_SHIPPING_THRESHOLD - cart_total
    return f"Add {missing:.2f} EUR for free shipping"


def render_cart(cart):
    total = sum(item.price * item.quantity for item in cart.items)
    return {
        "banner": shipping_banner(total),
        "fee": shipping_fee(total),
        "items": [item.as_row() for item in cart.items],
    }

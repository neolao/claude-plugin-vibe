from .discount import compute_discount_cents


def apply_promo(cart, promo):
    """Called once per checkout when the customer enters a promo code."""
    discount = compute_discount_cents(cart["subtotal_cents"], promo["kind"], promo["value"])
    return {
        "subtotal_cents": cart["subtotal_cents"],
        "discount_cents": discount,
        "total_cents": cart["subtotal_cents"] - discount,
    }

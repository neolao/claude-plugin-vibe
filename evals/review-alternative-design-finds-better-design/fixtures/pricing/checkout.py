from .describe import describe_discount
from .rules import compute_discount_cents
from .validate import validate_discount


def apply_promo(cart, promo):
    """Called once per checkout when the customer enters a promo code."""
    if not validate_discount(promo["kind"], promo["value"]):
        raise ValueError("invalid promo")
    discount = compute_discount_cents(cart["subtotal_cents"], promo["kind"], promo["value"])
    return {
        "subtotal_cents": cart["subtotal_cents"],
        "discount_cents": discount,
        "label": describe_discount(promo["kind"], promo["value"]),
        "total_cents": cart["subtotal_cents"] - discount,
    }

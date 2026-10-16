"""Promotions applicable to new orders."""

ACTIVE_PROMOTIONS = []


def configure_promotions(promotions):
    """Called by the entry point at startup."""
    ACTIVE_PROMOTIONS.extend(promotions)


def discount_for(order):
    """Best promotion discount for this order, in cents."""
    best = 0
    for promotion in ACTIVE_PROMOTIONS:
        if promotion.applies_to(order):
            best = max(best, promotion.discount_cents(order))
    return best

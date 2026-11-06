"""Promo codes: a percentage off the subtotal, capped per order."""

PROMO_PERCENT = {"WELCOME10": 10, "SPRING15": 15}
CAP_CENTS = 5_000


def discount_for(code: str | None, subtotal_cents: int) -> int:
    if code is None or code not in PROMO_PERCENT:
        return 0
    return min(subtotal_cents * PROMO_PERCENT[code] // 100, CAP_CENTS)

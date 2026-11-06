"""Order total: line amounts minus the discount, never below zero, VAT once at the end."""

VAT_RATE = 0.2


def calculate_total(line_amounts_cents: list[int], discount_cents: int = 0) -> int:
    subtotal = sum(line_amounts_cents) - discount_cents
    if subtotal < 0:
        subtotal = 0
    return int(round(subtotal * (1 + VAT_RATE)))

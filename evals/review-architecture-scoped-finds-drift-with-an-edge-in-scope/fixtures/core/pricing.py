"""Order total: line amounts summed, VAT once at the end."""

VAT_PERCENT = 20


def calculate_total(line_amounts_cents: list[int]) -> int:
    subtotal = sum(line_amounts_cents)
    return subtotal + subtotal * VAT_PERCENT // 100

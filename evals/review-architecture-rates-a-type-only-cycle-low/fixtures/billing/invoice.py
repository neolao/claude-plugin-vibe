"""Invoice of an order: line amounts, delivery fee, VAT once at the end."""

from dataclasses import dataclass

from shipping.schedule import delivery_fee_cents

VAT_PERCENT = 20


@dataclass(frozen=True)
class Invoice:
    order_id: str
    country: str
    total_cents: int


def build_invoice(order_id: str, line_amounts_cents: list[int], country: str) -> Invoice:
    subtotal = sum(line_amounts_cents) + delivery_fee_cents(country)
    return Invoice(order_id, country, subtotal + subtotal * VAT_PERCENT // 100)

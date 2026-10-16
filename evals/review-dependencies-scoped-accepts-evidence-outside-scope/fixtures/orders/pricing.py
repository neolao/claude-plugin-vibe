"""Prices a basket. Called by the checkout flow, the CLI and the receivables report."""
from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

VAT_RATE = Decimal("0.20")


@dataclass(frozen=True)
class Line:
    sku: str
    unit_price_cents: int
    quantity: int


def line_total_cents(line: Line) -> int:
    return line.unit_price_cents * line.quantity


def basket_total_cents(lines: list[Line], discount_percent: int = 0) -> int:
    subtotal = sum(line_total_cents(line) for line in lines)
    discounted = Decimal(subtotal) * (Decimal(100 - discount_percent) / Decimal(100))
    with_vat = discounted * (Decimal(1) + VAT_RATE)
    return int(with_vat.quantize(Decimal("1"), rounding=ROUND_HALF_UP))

"""Delivery fees per country and the estimated delivery date of an invoiced order."""

from __future__ import annotations

from datetime import date, timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from billing.invoice import Invoice

FEE_CENTS = {"FR": 490, "DE": 690, "ES": 790}
TRANSIT_DAYS = {"FR": 2, "DE": 3, "ES": 4}


def delivery_fee_cents(country: str) -> int:
    return FEE_CENTS.get(country, 990)


def eta_for(invoice: Invoice, today: date) -> date:
    return today + timedelta(days=TRANSIT_DAYS.get(invoice.country, 6))

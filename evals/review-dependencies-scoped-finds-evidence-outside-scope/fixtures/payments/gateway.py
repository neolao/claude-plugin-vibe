"""Payment provider client. Called by the checkout flow once the basket is priced."""
import os

import httpx

from orders.pricing import Line, basket_total_cents

PROVIDER_URL = os.environ.get("PAYMENT_PROVIDER_URL", "https://psp.example.com/v1")


def charge(customer_id: str, lines: list[Line], discount_percent: int = 0) -> str:
    amount_cents = basket_total_cents(lines, discount_percent)
    response = httpx.post(
        f"{PROVIDER_URL}/charges",
        json={"customer": customer_id, "amount": amount_cents, "currency": "EUR"},
        timeout=10.0,
    )
    response.raise_for_status()
    return response.json()["charge_id"]

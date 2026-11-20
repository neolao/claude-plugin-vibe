"""Fetches the next job's data from the billing API and renders its invoice."""
import os

import requests

API_URL = os.environ.get("BILLING_API_URL", "https://billing.internal/api")
TIMEOUT_SECONDS = 10


def _headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {os.environ['BILLING_API_TOKEN']}"}


def render_next(queue: str) -> bool:
    """Returns False when the queue is empty."""
    job = requests.post(f"{API_URL}/queues/{queue}/pop", headers=_headers(), timeout=TIMEOUT_SECONDS)
    job.raise_for_status()
    if job.status_code == 204:
        return False
    invoice = job.json()
    customer = requests.get(f"{API_URL}/customers/{invoice['customer_id']}", headers=_headers(), timeout=TIMEOUT_SECONDS)
    customer.raise_for_status()
    render_pdf(invoice, customer.json())
    return True


def render_pdf(invoice: dict, customer: dict) -> bytes:
    lines = "\n".join(f"{line['label']}: {line['amount']:.2f}" for line in invoice["lines"])
    return f"{customer['name']}\n{lines}".encode()

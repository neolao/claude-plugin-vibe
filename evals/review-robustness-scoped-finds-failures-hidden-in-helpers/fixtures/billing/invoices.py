from net.retry import with_retries

BILLING_API = "https://billing.example.com"


def fetch_invoice(session, invoice_id):
    """Called by the nightly reconciliation job for each open invoice."""
    response = with_retries(
        lambda: session.get(f"{BILLING_API}/invoices/{invoice_id}", timeout=5)
    )
    response.raise_for_status()
    return response.json()

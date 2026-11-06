"""HTTP handlers of the invoice API; called by the router for each request."""
import csv
from datetime import date

ALLOWED_CURRENCIES = ("EUR", "USD", "GBP")

EXPORT_DIR = "/var/exports"


def validate_invoice(payload):
    errors = []
    if payload.get("currency") not in ALLOWED_CURRENCIES:
        errors.append("currency must be one of EUR, USD, GBP")
    if payload.get("amount_cents", 0) <= 0:
        errors.append("amount must be positive")
    return errors


def export_invoice(invoice):
    name = f"invoice-{invoice.reference}-{date.today():%Y%m%d}.csv"
    with open(f"{EXPORT_DIR}/{name}", "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["reference", "currency", "amount_cents"])
        writer.writerow([invoice.reference, invoice.currency, invoice.amount_cents])
    return name

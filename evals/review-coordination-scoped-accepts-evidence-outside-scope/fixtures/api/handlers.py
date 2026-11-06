"""HTTP handlers of the invoice API; called by the router for each request."""
import csv
from datetime import date

from core.currencies import ALLOWED_CURRENCIES
from core.filenames import invoice_filename

EXPORT_DIR = "/var/exports"


def validate_invoice(payload):
    errors = []
    if payload.get("currency") not in ALLOWED_CURRENCIES:
        errors.append(f"currency must be one of {', '.join(ALLOWED_CURRENCIES)}")
    if payload.get("amount_cents", 0) <= 0:
        errors.append("amount must be positive")
    return errors


def export_invoice(invoice):
    name = invoice_filename(invoice.reference, date.today())
    with open(f"{EXPORT_DIR}/{name}", "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["reference", "currency", "amount_cents"])
        writer.writerow([invoice.reference, invoice.currency, invoice.amount_cents])
    return name

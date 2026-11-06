"""Builds the CSV export of an account's invoices for a month. Called from app.py on request."""

from adapters.s3_storage import upload


def export_account_csv(account_id, month, invoices):
    rows = invoices.for_month(account_id, month)
    csv = "id,amount\n" + "\n".join(f"{row.id},{row.amount}" for row in rows)
    key = f"exports/{account_id}/{month}.csv"
    upload(key, csv.encode())
    return key

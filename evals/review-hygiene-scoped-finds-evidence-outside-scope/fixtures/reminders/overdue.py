"""Selection of the invoices that get a reminder."""
from datetime import timedelta


def overdue_invoices(invoices, today):
    return [
        invoice
        for invoice in invoices
        if invoice["issued"] + timedelta(days=30) < today
    ]

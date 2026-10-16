"""Nightly job: numbers the invoices of the day, run by the scheduler."""
from datetime import date

from billing import InvoiceNumberSequence


def number_pending_invoices(pending, last_issued):
    sequence = InvoiceNumberSequence(date.today().year, last_issued)
    for invoice in pending:
        invoice["number"] = sequence.next()
    return sequence.last_issued()

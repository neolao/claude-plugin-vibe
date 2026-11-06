"""Builds an invoice for an order and stores it. Called from app.py on each new order."""

from adapters.s3_storage import upload
from core.pricing import total


def issue_invoice(order, invoices):
    invoice = invoices.create(order.account_id, total(order))
    pdf = render_invoice_pdf(invoice)
    upload(f"invoices/{invoice.id}.pdf", pdf)
    return invoice


def render_invoice_pdf(invoice):
    return f"INVOICE {invoice.id} {invoice.amount}".encode()

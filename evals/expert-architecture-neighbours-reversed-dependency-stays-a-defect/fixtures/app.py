"""HTTP routes and composition root. Called once at process start."""

from adapters.postgres_invoices import PostgresInvoices
from core.export_service import export_account_csv
from core.invoice_service import issue_invoice

invoices = PostgresInvoices.from_env()


def post_invoice(order):
    return issue_invoice(order, invoices)


def get_export(account_id, month):
    return export_account_csv(account_id, month, invoices)

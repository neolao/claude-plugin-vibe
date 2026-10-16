"""Invoice text sent to the customer."""
from datetime import timedelta


def render_invoice(invoice):
    due = invoice["issued"] + timedelta(days=30)
    return "\n".join(
        [
            f"Invoice {invoice['number']} for {invoice['customer']}",
            f"Issued: {invoice['issued'].isoformat()}",
            f"Due: {due.isoformat()}",
            f"Total: {_amount(invoice['total_cents'])}",
        ]
    )


def _amount(cents):
    return "%.2f EUR" % (cents / 100)

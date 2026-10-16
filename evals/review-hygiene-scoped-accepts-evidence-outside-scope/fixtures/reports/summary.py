"""Monthly figures, printed by the `summary` command."""
from billing.money import format_amount


def monthly_summary(invoices):
    total = sum(invoice["total_cents"] for invoice in invoices)
    return f"{len(invoices)} invoices, {format_amount(total)}"

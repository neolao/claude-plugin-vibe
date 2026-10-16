"""Receivables by age, printed by the `aging` command."""
from datetime import timedelta

from reports.money import format_amount


def aging_report(invoices, today):
    current = 0
    late = 0
    for invoice in invoices:
        if invoice["issued"] + timedelta(days=30) < today:
            late += invoice["total_cents"]
        else:
            current += invoice["total_cents"]
    return "\n".join(
        [
            f"Not yet due: {format_amount(current)}",
            f"Past due: {format_amount(late)}",
        ]
    )

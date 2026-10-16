"""Invoice export handed to the accounting software."""
import csv

from billing.money import format_amount


def export_invoices_csv(invoices, out):
    writer = csv.writer(out)
    writer.writerow(["number", "customer", "total", "issued"])
    for invoice in invoices:
        writer.writerow(
            [
                invoice["number"],
                invoice["customer"],
                format_amount(invoice["total_cents"]),
                invoice["issued"].isoformat(),
            ]
        )

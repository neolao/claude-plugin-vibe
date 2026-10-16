"""Invoice exports handed to the accounting software."""
import csv


def export_invoices_csv(invoices, out):
    writer = csv.writer(out)
    writer.writerow(["number", "customer", "total_cents", "issued"])
    for invoice in invoices:
        writer.writerow(
            [
                invoice["number"],
                invoice["customer"],
                invoice["total_cents"],
                invoice["issued"].isoformat(),
            ]
        )


def export_invoices_xml(invoices, out):
    out.write("<invoices>")
    for invoice in invoices:
        out.write(
            f'<invoice number="{invoice["number"]}" '
            f'customer="{invoice["customer"]}" '
            f'total_cents="{invoice["total_cents"]}" '
            f'issued="{invoice["issued"].isoformat()}"/>'
        )
    out.write("</invoices>")

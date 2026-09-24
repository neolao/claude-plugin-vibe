"""Order export, written to stdout by the `export` command."""
import csv

from billing.money import format_amount, subtotal_cents


def export_orders_csv(orders, out):
    writer = csv.writer(out)
    writer.writerow(["id", "customer", "total"])
    for order in orders:
        total = format_amount(subtotal_cents(order["lines"]))
        writer.writerow([order["id"], order["customer"], total])


def export_orders_xml(orders, out):
    out.write("<orders>")
    for order in orders:
        total = format_amount(subtotal_cents(order["lines"]))
        out.write(
            f'<order id="{order["id"]}" customer="{order["customer"]}" '
            f'total="{total}"/>'
        )
    out.write("</orders>")

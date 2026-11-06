"""Daily CSV export of every order, read by the accounting team."""
import csv

STATUS_LABELS = {
    "pending": "Pending",
    "paid": "Paid",
    "shipped": "Shipped",
}


def export_orders(orders, path):
    with open(path, "w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["reference", "status"])
        for order in orders:
            writer.writerow([order.reference, STATUS_LABELS[order.status]])

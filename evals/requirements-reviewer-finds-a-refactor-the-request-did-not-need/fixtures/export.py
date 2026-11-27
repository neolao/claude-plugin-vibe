"""Monthly report export. Called from the admin page."""

import csv
import io


def format_label(text):
    return " ".join(part.capitalize() for part in text.split())


def total_amount(rows):
    return round(sum(row["amount"] for row in rows), 2)


def to_csv(rows):
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["date", "amount", "label"])
    for row in rows:
        writer.writerow([row["date"], row["amount"], format_label(row["label"])])
    writer.writerow(["total", total_amount(rows)])
    return buf.getvalue()


def export_report(rows, month):
    return f"report-{month}.csv", to_csv(rows).encode("utf-8")

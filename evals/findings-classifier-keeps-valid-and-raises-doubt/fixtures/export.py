"""CSV export of the monthly report. Called from the admin page."""

import csv
import io


def to_csv(rows):
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["date", "amount", "label"])
    for row in rows:
        writer.writerow([row["date"], row["amount"], row["label"]])
    return buf.getvalue()


def export_report(rows):
    body = to_csv(rows)
    return body.encode("utf-8")

"""Monthly report export. Called from the admin page."""

import csv
import io
import json


def to_csv(rows):
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["date", "amount", "label"])
    for row in rows:
        writer.writerow([row["date"], row["amount"], row["label"]])
    return buf.getvalue()


def to_json(rows):
    return json.dumps(rows, indent=2)


def export_report(rows, month, fmt="csv"):
    if fmt == "json":
        body = to_json(rows)
        name = f"report-{month}.json"
    else:
        body = to_csv(rows)
        name = f"report-{month}.csv"
    return name, body.encode("utf-8")

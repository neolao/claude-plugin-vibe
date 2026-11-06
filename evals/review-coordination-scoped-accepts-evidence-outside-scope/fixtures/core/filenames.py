"""Name of a CSV export: `invoice-<reference>-<YYYYMMDD>.csv`."""
from datetime import date


def invoice_filename(reference, day):
    return f"invoice-{reference}-{day:%Y%m%d}.csv"


def parse_invoice_filename(name):
    if not name.startswith("invoice-") or not name.endswith(".csv"):
        return None
    _, reference, stamp = name[:-4].split("-")
    return reference, date(int(stamp[:4]), int(stamp[4:6]), int(stamp[6:]))

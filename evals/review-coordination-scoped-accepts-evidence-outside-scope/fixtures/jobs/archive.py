"""Nightly job: moves the day's CSV exports into the archive tree, one folder per day."""
import os
import shutil

from core.filenames import parse_invoice_filename

EXPORT_DIR = "/var/exports"
ARCHIVE_DIR = "/var/archive"


def archive_exports():
    for name in os.listdir(EXPORT_DIR):
        parsed = parse_invoice_filename(name)
        if parsed is None:
            continue
        reference, day = parsed
        target = f"{ARCHIVE_DIR}/{day:%Y/%m/%d}"
        os.makedirs(target, exist_ok=True)
        shutil.move(f"{EXPORT_DIR}/{name}", f"{target}/{reference}.csv")

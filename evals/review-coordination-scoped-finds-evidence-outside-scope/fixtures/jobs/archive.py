"""Nightly job: moves the day's CSV exports into the archive tree, one folder per day."""
import os
import shutil

EXPORT_DIR = "/var/exports"
ARCHIVE_DIR = "/var/archive"


def archive_exports():
    for name in os.listdir(EXPORT_DIR):
        if not name.endswith(".csv"):
            continue
        _, reference, stamp = name[:-4].split("-")
        target = f"{ARCHIVE_DIR}/{stamp[:4]}/{stamp[4:6]}/{stamp[6:]}"
        os.makedirs(target, exist_ok=True)
        shutil.move(f"{EXPORT_DIR}/{name}", f"{target}/{reference}.csv")

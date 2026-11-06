"""Nightly job: deletes archived exports older than the retention period."""
import os
import time

ARCHIVE_DIR = "/var/archive"
RETENTION_DAYS = 90


def purge_archive():
    limit = time.time() - RETENTION_DAYS * 86400
    for root, _, files in os.walk(ARCHIVE_DIR):
        for name in files:
            path = f"{root}/{name}"
            if os.path.getmtime(path) < limit:
                os.remove(path)

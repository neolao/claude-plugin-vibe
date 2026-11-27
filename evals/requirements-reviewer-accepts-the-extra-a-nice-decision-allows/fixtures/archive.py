"""Archive of old transactions. Run by the nightly scheduler."""

import logging
from datetime import date

from scheduler import every_night

log = logging.getLogger("archive")

MONTHS_KEPT = 24


class Ledger:
    def __init__(self, live):
        self.live = list(live)
        self.archive = []
        self.last_moved_ids = []


def months_between(start, end):
    return (end.year - start.year) * 12 + end.month - start.month


def archive_old(ledger, today, dry_run=False):
    old = [row for row in ledger.live if months_between(row["date"], today) > MONTHS_KEPT]
    if dry_run:
        return len(old)
    ledger.live = [row for row in ledger.live if row not in old]
    ledger.archive.extend(old)
    ledger.last_moved_ids = [row["id"] for row in old]
    log.info("archived %d transactions", len(old))
    return len(old)


def register(ledger):
    every_night(2, lambda: archive_old(ledger, date.today()))

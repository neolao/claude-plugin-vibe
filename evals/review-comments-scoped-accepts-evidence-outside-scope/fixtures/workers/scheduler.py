"""Runs the polling loop every ten minutes and logs what it could not fetch."""
import logging
import time

from sync.poller import poll

log = logging.getLogger("supplier-sync")
PERIOD = 600


def run_forever(queue):
    while True:
        try:
            poll(queue)
        except RuntimeError as error:
            log.warning("poll skipped: %s", error)
        time.sleep(PERIOD)

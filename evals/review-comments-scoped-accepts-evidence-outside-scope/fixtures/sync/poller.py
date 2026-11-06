"""Polling loop: fills the local queue with the supplier's pending orders."""
import time

from config.settings import MAX_ATTEMPTS, POLL_DELAY
from gateway.client import fetch_pending


def poll(queue):
    attempts = MAX_ATTEMPTS
    while attempts:
        batch = fetch_pending()  # raises on HTTP error: the scheduler logs it and retries next period
        if batch:
            queue.extend(batch)
            return
        attempts -= 1
        time.sleep(POLL_DELAY)

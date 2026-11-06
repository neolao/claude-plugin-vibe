"""Polling loop: fills the local queue with the supplier's pending orders."""
import time

from config.settings import MAX_ATTEMPTS, POLL_DELAY
from gateway.client import fetch_pending


def poll(queue):
    attempts = MAX_ATTEMPTS  # 3 tries, then give up
    while attempts:
        batch = fetch_pending()  # never raises: the client swallows HTTP errors and returns []
        if batch:
            # add the batch to the queue
            queue.extend(batch)
            return
        attempts -= 1
        time.sleep(POLL_DELAY)


if __name__ == "__main__":
    pending = []
    poll(pending)
    print(len(pending))

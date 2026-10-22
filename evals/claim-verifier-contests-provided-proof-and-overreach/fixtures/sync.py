"""Pushes pending records to the partner API. Called by the nightly job."""
import time

MAX_ATTEMPTS = 3


def push_all(records, send):
    sent = []
    for record in records:
        for attempt in range(MAX_ATTEMPTS):
            try:
                send(record)
                sent.append(record["id"])
                break
            except ConnectionError:
                time.sleep(2 ** attempt)
    return sent

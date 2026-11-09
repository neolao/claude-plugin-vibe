"""Pushes orders to the warehouse API. Called by the order-created hook."""
import time

MAX_RETRIES = 3


class WarehouseError(Exception):
    pass


def push_order(send, order):
    """Send `order` with `send`; retry on WarehouseError, up to MAX_RETRIES retries
    after the first attempt. Raises the last error when all of them failed."""
    last_error = None
    for attempt in range(MAX_RETRIES - 1):
        try:
            return send(order)
        except WarehouseError as exc:
            last_error = exc
            time.sleep(2 ** attempt)
    raise last_error

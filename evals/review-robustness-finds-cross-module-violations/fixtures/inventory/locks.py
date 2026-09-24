import threading
from collections import defaultdict

_per_sku = defaultdict(threading.Lock)


def hold(sku: str) -> threading.Lock:
    """Serializes writes to one SKU between the scheduler and the back office."""
    lock = _per_sku[sku]
    lock.acquire()
    return lock

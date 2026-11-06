"""In-memory warehouse levels; LOCK serialises every read-modify-write."""
import threading

LEVELS = {}
LOCK = threading.Lock()


def level(sku):
    return LEVELS.get(sku, 0)


def set_level(sku, qty):
    LEVELS[sku] = qty

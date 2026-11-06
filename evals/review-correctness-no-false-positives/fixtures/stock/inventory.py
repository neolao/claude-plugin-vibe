"""In-memory stock of the warehouse; read and written by the HTTP handlers."""
import threading

_levels = {}
_lock = threading.Lock()


def set_level(sku, qty):
    with _lock:
        _levels[sku] = qty


def level(sku):
    with _lock:
        return _levels.get(sku, 0)


def reserve(sku, qty):
    """Reserve qty units of sku for an order; False when not enough is left."""
    with _lock:
        available = _levels.get(sku, 0)
        if available < qty:
            return False
        _levels[sku] = available - qty
        return True

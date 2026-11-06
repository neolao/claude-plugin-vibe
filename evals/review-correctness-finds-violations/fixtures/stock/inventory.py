"""In-memory stock of the warehouse; read and written by the HTTP handlers."""
from catalog.sku import normalize_sku

_levels = {}


def set_level(sku, qty):
    _levels[normalize_sku(sku)] = qty


def level(sku):
    return _levels.get(normalize_sku(sku), 0)


def reserve(sku, qty):
    """Reserve qty units of sku for an order; False when not enough is left."""
    available = level(sku)
    if available < qty:
        return False
    set_level(sku, available - qty)
    return True

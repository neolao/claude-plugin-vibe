"""Stock reservations taken at checkout; called from the HTTP handlers."""
from inventory.stock import level, set_level


def reserve(sku, qty):
    """Reserve qty units of sku for an order; False when not enough is left."""
    available = level(sku)
    if available < qty:
        return False
    set_level(sku, available - qty)
    return True

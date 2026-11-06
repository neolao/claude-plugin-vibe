"""In-memory warehouse levels keyed by canonical SKU."""
from catalog.sku import normalize_sku

LEVELS = {}


def level(sku):
    return LEVELS.get(normalize_sku(sku), 0)


def set_level(sku, qty):
    LEVELS[normalize_sku(sku)] = qty

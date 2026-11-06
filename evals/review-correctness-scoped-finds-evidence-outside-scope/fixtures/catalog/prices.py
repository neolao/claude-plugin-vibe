"""Price list keyed by canonical SKU, filled by the nightly import."""
from catalog.sku import normalize_sku

PRICES = {}


def price_of(sku):
    """Unit price of a SKU as typed on the order form."""
    return PRICES[normalize_sku(sku)]

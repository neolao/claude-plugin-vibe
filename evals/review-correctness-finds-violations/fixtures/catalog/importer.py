"""Nightly import of the supplier's price list (one SKU and one price per row)."""
from catalog.sku import normalize_sku

prices = {}


def import_rows(rows):
    for raw_sku, price in rows:
        prices[normalize_sku(raw_sku.strip())] = float(price)


def price_of(sku):
    return prices[normalize_sku(sku)]

_price_cache = {}


def get_price(sku, catalog_service):
    """Called from the product-detail request handler on every page view."""
    if sku not in _price_cache:
        _price_cache[sku] = catalog_service.fetch_price(sku)
    return _price_cache[sku]

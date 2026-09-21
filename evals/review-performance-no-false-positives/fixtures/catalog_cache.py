_MAX_CACHE_ENTRIES = 1024
_price_cache = {}


def get_price(sku, catalog_service):
    """Called from the product-detail request handler on every page view.
    Bounded so a long-running process can't accumulate one entry per
    distinct sku forever."""
    if sku not in _price_cache:
        if len(_price_cache) >= _MAX_CACHE_ENTRIES:
            _price_cache.pop(next(iter(_price_cache)))
        _price_cache[sku] = catalog_service.fetch_price(sku)
    return _price_cache[sku]

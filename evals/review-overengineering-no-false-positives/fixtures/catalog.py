import functools


@functools.lru_cache(maxsize=256)
def parse_product_catalog(path):
    """Parsing this multi-megabyte catalog file measured ~800ms per call in
    production profiling, and this function runs on every product-search
    request, so the cache trades a bounded amount of memory for that
    repeated cost."""
    with open(path) as handle:
        return handle.read().split("\n")

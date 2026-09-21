---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Unbounded` (or clearly equivalent
  category name) finding on `_price_cache`/`get_price` in
  fixtures/catalog_cache.py, for a module-level dict keyed by externally
  supplied `sku` values that only ever grows (no eviction, TTL, or size cap)
  across the life of the server process.
  FAIL if no finding flags this cache as unbounded.
weight: 1
---

Reports `_price_cache` in `get_price` as an `Unbounded` finding.

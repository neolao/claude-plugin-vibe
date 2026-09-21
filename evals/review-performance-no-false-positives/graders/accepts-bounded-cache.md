---
type: llm
focus: last_message
criteria: |
  `_price_cache` in fixtures/catalog_cache.py is keyed by externally
  supplied skus, but `get_price` evicts an entry once `_MAX_CACHE_ENTRIES`
  is reached, so the dict cannot grow without bound.

  PASS if no `high` or `medium` severity finding calls this cache unbounded
  or a memory leak.
  FAIL if it is flagged as Unbounded (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a size-capped, evicting cache unbounded.

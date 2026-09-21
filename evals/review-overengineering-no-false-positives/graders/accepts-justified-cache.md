---
type: llm
focus: last_message
criteria: |
  The `lru_cache` on `parse_product_catalog` carries a stated measured cost
  (~800ms per call, on every product-search request).

  PASS if no `high` or `medium` severity Premature optimization finding
  targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a cache with a measured justification premature.

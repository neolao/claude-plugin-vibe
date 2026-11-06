---
type: llm
focus: last_message
criteria: |
  `normalize_sku` in fixtures/catalog/sku.py (outside the scope) promises
  "upper case, no surrounding blanks" but only upper-cases. `import_rows`
  in fixtures/orders/importer.py (in scope) compensates by calling
  `normalize_sku(raw_sku.strip())`, while `price_of`
  (fixtures/catalog/prices.py) and `level`/`set_level`
  (fixtures/inventory/stock.py) pass the SKU raw, and the handlers in
  fixtures/app/server.py hand them what a clerk typed.

  PASS if the reported findings include a `Wrong altitude` (or clearly
  equivalent category name) finding anchored on fixtures/orders/importer.py
  whose SUGGESTION places the trim in `normalize_sku` (fixtures/catalog/sku.py)
  rather than at more call sites, and which names at least one other
  caller (`price_of`, `level`, `set_level`, fixtures/catalog/prices.py or
  fixtures/inventory/stock.py) still affected: a SKU typed with a leading
  or trailing blank misses the price or stock it was imported under.
  FAIL if no finding names the trim missing from `normalize_sku`, if the
  finding is anchored on fixtures/catalog/sku.py, or if the only
  suggestion is to add `.strip()` at more call sites.
weight: 2
---

Reports the fix that sits at the in-scope call site while the helper,
outside the scope, keeps the defect for its other callers — anchored on
the caller, with the helper named as the right altitude.

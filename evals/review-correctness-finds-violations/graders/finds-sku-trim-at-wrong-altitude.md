---
type: llm
focus: last_message
criteria: |
  `normalize_sku` in fixtures/catalog/sku.py promises "upper case, no
  surrounding blanks" but only upper-cases. `import_rows` in
  fixtures/catalog/importer.py compensates by calling
  `normalize_sku(raw_sku.strip())`, while `price_of` in the same file and
  `level`/`set_level`/`reserve` in fixtures/stock/inventory.py pass the
  SKU raw, and the `/reserve` and `/checkout` handlers in
  fixtures/api/app.py hand them what a clerk typed.

  PASS if the reported findings include a `Wrong altitude` (or clearly
  equivalent category name, such as `Wrong logic` on `normalize_sku`)
  finding, anchored on fixtures/catalog/sku.py or
  fixtures/catalog/importer.py, that places the fix in `normalize_sku`
  (the shared helper) rather than at the call sites, and names at least
  one other caller (`price_of`, `reserve`, `level` or
  fixtures/stock/inventory.py) still affected: a SKU typed with a
  leading or trailing blank misses the stock or price it was imported
  under.
  FAIL if no finding names the trim missing from `normalize_sku`, or if
  the only suggestion is to add `.strip()` at more call sites.
weight: 2
---

Reports the fix that sits at one call site while the shared helper keeps
the defect for its other callers, and puts the fix in the helper.

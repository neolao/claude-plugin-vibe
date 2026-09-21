---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Blocking` (or clearly equivalent
  category name) finding on `load_warehouse_config` in
  fixtures/inventory_service.py, for synchronously reading and parsing a file
  from disk inline on every request handled by the reservations endpoint,
  instead of caching or loading it once.
  FAIL if no finding flags this synchronous file I/O on the request path.
weight: 1
---

Reports the per-request synchronous file read/parse in
`load_warehouse_config` as a `Blocking` finding.

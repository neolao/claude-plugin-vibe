---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Resource` (or clearly equivalent
  category name) finding on `sync_skus` (fixtures/inventory/jobs.py) for
  releasing the per-SKU lock without `try`/`finally`: `locks.hold`
  (fixtures/inventory/locks.py) acquires a `threading.Lock`, and when
  `client.stock_level` raises (any supplier network error), `lock.release()`
  is skipped, so that SKU's lock stays held and the next sync or back-office
  update of that SKU blocks forever.
  FAIL if no finding flags this unguarded lock release in `sync_skus`.
weight: 1
---

Reports the lock taken by `locks.hold` and released outside a `finally` in
`sync_skus`. jobs.py alone shows a returned object; only locks.py shows it is
an acquired lock.

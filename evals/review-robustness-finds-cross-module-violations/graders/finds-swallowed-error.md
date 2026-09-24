---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Swallowed error` (or clearly
  equivalent category name) finding for the sync path discarding a failed
  write: `ledger.apply` (fixtures/inventory/ledger.py) catches
  `sqlite3.Error`, logs a warning and returns `False`, and `sync_skus`
  (fixtures/inventory/jobs.py) ignores that return value and still appends
  the SKU to `consumed`, which `run` passes to `cursor.advance`, so the
  supplier's change is marked consumed and the level is never retried. The finding may be anchored in ledger.py or
  jobs.py, as long as it names the sync path going on after the failed write.
  A finding only about `api.adjust_stock` does not count: that caller checks
  the return value.
  FAIL if no finding flags this ignored failure on the sync path.
weight: 2
---

Reports `sync_skus` ignoring `ledger.apply`'s `False` and advancing the
cursor past that SKU anyway. ledger.py alone logs and returns a status; only jobs.py shows
that nobody on the sync path reads it.

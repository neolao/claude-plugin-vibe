---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Lost context` (or clearly
  equivalent category name) finding for the sync failure losing its cause:
  `jobs.run` (fixtures/inventory/jobs.py) wraps the `SupplierError` in
  `SyncFailed(exc)`, whose constructor (fixtures/inventory/errors.py) drops
  the cause and keeps only "inventory sync failed", and `worker.tick`
  (fixtures/inventory/worker.py) logs that message with `%s` and no
  traceback — so the log line never says which SKU failed or why. The
  finding may be anchored in errors.py, jobs.py or worker.py, as long as it
  names this `SyncFailed` path losing the supplier error's SKU or cause.
  FAIL if no finding flags this lost context.
weight: 1
---

Reports the `SyncFailed` wrapping that drops the supplier error's SKU and
cause before `worker.tick` logs it.

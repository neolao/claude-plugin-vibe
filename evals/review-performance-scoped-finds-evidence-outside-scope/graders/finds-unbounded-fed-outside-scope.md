---
type: llm
focus: last_message
criteria: |
  `record_scan` in fixtures/shipping/tracking.py writes the module-level
  `_latest` dict, keyed by tracking number; `carrier_webhook` in
  fixtures/api/app.py, outside the scope, feeds it one entry per parcel
  ever scanned, and nothing calls `forget_delivered` (defined in the same
  file), so the dict grows for the life of the process.

  PASS if the reported findings include an `Unbounded` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/shipping/tracking.py, that names `_latest` (or `record_scan`)
  as growing without bound, and whose ISSUE or SUGGESTION names
  `carrier_webhook` or fixtures/api/app.py as the feeder, or says that
  nothing calls `forget_delivered`.
  FAIL if no finding reports `_latest` as growing without bound, or if the
  finding is anchored (its FILE: line) on fixtures/api/app.py.
weight: 1
---

Reports the map declared in scope as Unbounded, with the outside webhook
as the feeder and the uncalled pruning function as evidence.

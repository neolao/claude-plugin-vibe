---
type: llm
focus: last_message
criteria: |
  `record_scan` in fixtures/shipping/tracking.py writes the module-level
  `_latest` dict that `carrier_webhook` in fixtures/api/app.py feeds;
  `prune_scans` in fixtures/api/jobs.py (outside the scope), scheduled
  every night, calls `forget_delivered` on it, so the dict holds at most
  the parcels in transit plus a week of delivered ones.

  PASS if no `high` or `medium` severity `Unbounded` (or clearly
  equivalent category name) finding targets `_latest` or `record_scan`. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if `_latest` is reported as growing without bound, never evicted or
  a memory leak at high or medium severity.
weight: 1
---

Does not call a map Unbounded when a job outside the scope prunes it.

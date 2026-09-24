---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Unbounded` (or clearly equivalent
  category name) finding on the module-level `_latest` dict in
  fixtures/shipping/tracking.py, keyed by tracking numbers that arrive from
  the carrier webhook (`carrier_webhook` in fixtures/shipping/app.py), which
  gains one entry per parcel ever scanned and is never evicted or capped for
  the life of the process.
  FAIL if no finding flags `_latest` as growing without bound.
weight: 1
---

Reports the webhook-fed `_latest` dict in tracking.py as `Unbounded`.

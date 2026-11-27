---
type: llm
focus: last_message
criteria: |
  `zone_for` in fixtures/shipping/zones.py scans the ~3 000-entry
  `_DISTRICTS` list linearly. Its only caller, `on_startup` in
  fixtures/api/app.py (outside the scope), runs it once per warehouse of
  the three in `WAREHOUSES` when the server starts, before it accepts
  requests; nothing calls `price_cents`.

  PASS if no `high` or `medium` severity `Complexity` (or clearly
  equivalent category name) finding targets `zone_for`, `price_cents` or
  the `_DISTRICTS` scan. A `low` finding passes, and so does a report with
  no findings at all.
  FAIL if the linear scan is reported as a repeated or hot-path search at
  high or medium severity.
weight: 1
---

Does not call a linear scan a Complexity defect when its only caller,
outside the scope, runs it three times at startup.

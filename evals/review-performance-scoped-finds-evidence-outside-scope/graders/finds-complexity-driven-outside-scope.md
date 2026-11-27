---
type: llm
focus: last_message
criteria: |
  `zone_for` in fixtures/shipping/zones.py scans the ~3 000-entry
  `_DISTRICTS` list linearly on every call; `bulk_quote` in
  fixtures/api/app.py, outside the scope, calls `zones.price_cents` (hence
  `zone_for`) once per parcel, up to 5 000 parcels per request, where a
  dict keyed by district gives an O(1) lookup.

  PASS if the reported findings include a `Complexity` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/shipping/zones.py, that names the linear scan of `_DISTRICTS`
  in `zone_for`, and whose ISSUE or SUGGESTION names `bulk_quote`,
  fixtures/api/app.py or the 5 000 parcels per call as what makes it hot.
  FAIL if no finding reports this repeated linear search, or if the
  finding is anchored (its FILE: line) on fixtures/api/app.py.
weight: 1
---

Reports the linear scan declared in scope, with the outside bulk caller
as the SCALE evidence.

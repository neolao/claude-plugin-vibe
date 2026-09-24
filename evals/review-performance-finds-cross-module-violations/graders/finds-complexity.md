---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Complexity` (or clearly equivalent
  category name) finding on `zone_for` in fixtures/shipping/zones.py, for
  scanning the ~3 000-entry `_DISTRICTS` list linearly on every lookup, which
  `bulk_quote` in fixtures/shipping/app.py calls once per parcel (up to 5 000
  per request), where a dict keyed by district gives an O(1) lookup.
  FAIL if no finding flags this repeated linear search.
weight: 1
---

Reports the linear district scan in `zone_for`, driven per parcel by
`bulk_quote`, as a `Complexity` finding.

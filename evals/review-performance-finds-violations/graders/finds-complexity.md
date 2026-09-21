---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Complexity` (or clearly equivalent
  category name) finding on `has_conflicting_reservation` in
  fixtures/inventory_service.py, for doing a linear scan over
  `existing_reservations` on every call from a request handler, where a
  structure keyed by `(warehouse, slot)` would give an O(1) lookup instead.
  FAIL if no finding flags this repeated linear search.
weight: 1
---

Reports the repeated linear scan in `has_conflicting_reservation` as a
`Complexity` finding.

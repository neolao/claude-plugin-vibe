---
type: llm
focus: last_message
criteria: |
  `has_conflicting_reservation` in fixtures/inventory_service.py builds a
  `(warehouse, slot)` tuple and tests membership in `reservations_by_slot`,
  a dict maintained by the caller — an O(1) lookup, not a scan.

  PASS if no `high` or `medium` severity finding calls this a linear search
  or a complexity problem.
  FAIL if it is flagged as Complexity (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a dict membership test a linear scan.

---
type: llm
focus: last_message
criteria: |
  `reserve` in fixtures/orders/reservations.py reads the level, compares
  it with `qty` and writes the new level with no lock of its own; its only
  caller, the `/reserve` handler in fixtures/app/server.py (outside the
  scope), calls it inside `with LOCK:` (fixtures/inventory/stock.py), so
  the check and the write never overlap between two requests.

  PASS if no `high` or `medium` severity finding claims `reserve` has a
  check-then-act race or that two concurrent reservations can both
  succeed on the last units.
  FAIL if it is flagged as a Race issue (or equivalent) at high or medium
  severity.
weight: 1
---

Does not flag a check-then-act whose only caller, outside the scope,
holds the lock around the whole call.

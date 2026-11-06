---
type: llm
focus: last_message
criteria: |
  `reserve` in fixtures/stock/inventory.py reads the level, compares it
  with `qty` and writes the new level inside one `with _lock:` block, and
  `level`/`set_level` take the same lock; the server is multi-threaded.

  PASS if no `high` or `medium` severity finding claims `reserve` has a
  check-then-act race or that two concurrent reservations can both
  succeed on the last units.
  FAIL if it is flagged as a Race issue (or equivalent) at high or medium
  severity.
weight: 1
---

Does not flag a check-then-act held under a lock for both steps.

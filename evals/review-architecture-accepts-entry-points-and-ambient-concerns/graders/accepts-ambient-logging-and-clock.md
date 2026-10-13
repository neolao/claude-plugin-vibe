---
type: llm
focus: last_message
criteria: |
  `core/order_service.py` imports the standard library `logging` and `datetime` to log a timestamped line. No port exists for either and no decision requires one.

  PASS if no `high` or `medium` severity Layer direction, Port ownership, Wiring, or Decision violated finding targets those standard-library imports.
  FAIL if it is reported at high or medium severity.
weight: 1
---

Does not call ambient logging and clock use a layer violation.

---
type: llm
focus: last_message
criteria: |
  `PostgresGateway.save` catches `psycopg2.Error` and re-raises it as
  `OrderPersistenceError`, which `fixtures/core/ports.py` declares next to
  the port. No driver exception crosses the port boundary.

  PASS if no `high` or `medium` severity Leaky port finding claims driver or
  technology exceptions reach core through `save`.
  FAIL if one does at high or medium severity.
weight: 1
---

Does not call a port whose adapter translates driver errors into a core-owned
error leaky.

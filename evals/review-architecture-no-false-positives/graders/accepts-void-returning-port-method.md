---
type: llm
focus: last_message
criteria: |
  `PostgresGateway.save` returns `None` — no cursor, row, or driver type
  crosses the port boundary.

  PASS if no `high` or `medium` severity Leaky port finding targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a `None`-returning port implementation leaky.

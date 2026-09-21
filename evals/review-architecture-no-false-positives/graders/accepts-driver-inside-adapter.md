---
type: llm
focus: last_message
criteria: |
  `adapters/postgres_gateway.py` imports `psycopg2` and a DSN constant and
  runs SQL. That is what a driven adapter is for; decision 002 constrains
  `core/`, not `adapters/`. It calls no other adapter.

  PASS if no `high` or `medium` severity Layer direction, Adapter purity, or
  Decision violated finding targets it.
  FAIL if any does at high or medium severity.
weight: 1
---

Does not call an adapter's own driver usage a layering or decision violation.

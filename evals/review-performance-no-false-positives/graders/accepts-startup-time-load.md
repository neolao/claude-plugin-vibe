---
type: llm
focus: last_message
criteria: |
  `load_warehouse_config` in fixtures/inventory_service.py reads and parses
  a file, but its docstring states it runs once at process startup, before
  the server accepts requests, and is kept in memory afterwards.

  PASS if no `high` or `medium` severity finding claims this blocks a
  request path.
  FAIL if it is flagged as Blocking (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a startup-time config load request-path blocking I/O.

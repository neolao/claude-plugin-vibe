---
type: llm
focus: last_message
criteria: |
  `record_event` in fixtures/api.py is never called from inside its own
  package, but it is listed in the module's `__all__` and the module
  docstring states it is the package's public API consumed by other
  services.

  PASS if no `high` or `medium` severity finding calls `record_event` dead
  or unused code.
  FAIL if it is flagged as Dead code (or equivalent) at high or medium
  severity.
weight: 1
---

Does not call a declared public-API export dead code.

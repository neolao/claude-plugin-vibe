---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Module scope` (or clearly
  equivalent category name) finding on `core/order_service.py` (or the
  `core` module), for violating `.vibe/modules/core.md`'s declared role
  ("no I/O, no framework or database imports") by opening a database
  connection and executing SQL directly.
  FAIL if no finding flags this scope drift against the `core` module's
  declared role.
weight: 1
---

Reports `core/order_service.py`'s direct database I/O as a Module scope
drift finding against `.vibe/modules/core.md`.

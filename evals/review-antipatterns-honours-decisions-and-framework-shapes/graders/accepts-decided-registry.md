---
type: llm
focus: last_message
criteria: |
  The repo's `.vibe/decisions/001-import-time-handler-registry.md` (status
  accepted) mandates the module-level `HANDLERS` dict and the `register`
  function of fixtures/shop/handlers/__init__.py, filled at import time by
  fixtures/shop/handlers/billing.py and fixtures/shop/handlers/shipping.py;
  the code follows the decision.

  PASS if no `high` or `medium` severity Mutable global state (or
  equivalent) finding targets `HANDLERS`, `register`, or the handler
  modules' import-time registration. A report with no findings at all
  passes, as does a report that names the decision as the reason for
  staying silent.
  FAIL if the registry is flagged at high or medium severity.
weight: 2
---

Does not reopen a registry shape that a recorded decision settled.

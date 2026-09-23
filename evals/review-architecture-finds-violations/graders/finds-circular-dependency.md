---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Circular dependency` (or clearly
  equivalent category name) finding on the cycle between `core` and
  `adapters`: `fixtures/core/order_service.py` imports
  `adapters/postgres_gateway.py`, while `fixtures/adapters/email_notifier.py`
  imports `core/email_templates.py` (and `.vibe/modules/adapters.md`
  declares `adapters` depends on `core`) — a two-module cycle. Naming either
  import as the edge that closes the cycle is enough.
  FAIL if no finding flags this cycle.
weight: 1
---

Reports the core-adapters import cycle as a Circular dependency finding.

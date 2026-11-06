---
type: llm
focus: last_message
criteria: |
  No ADR, no `CLAUDE.md` and no `.vibe/decisions/` declare a hexagonal
  architecture; the tree alone does, with fixtures/core/ports/ holding
  `OrderGatewayPort` and fixtures/adapters/ holding its implementation.
  `NotifierPort` (an ABC) is defined in fixtures/adapters/smtp_notifier.py
  next to `SmtpNotifier`, and fixtures/core/order_service.py imports it
  from there.

  PASS if the reported findings include a `Port ownership` (or clearly
  equivalent category name) finding on `NotifierPort` being defined on the
  adapter side — anchored on fixtures/adapters/smtp_notifier.py or on
  fixtures/core/order_service.py's import of it — and the finding names
  the driven side (notifier, gateway, repository or equivalent wording).
  FAIL if no finding reports `NotifierPort`'s location as a port-ownership
  problem, or if the agent declines the ports & adapters section for lack
  of an ADR.
weight: 2
---

Reads the hexagon from `core/ports/` and `adapters/` without an ADR, and
reports the port defined on the adapter side.

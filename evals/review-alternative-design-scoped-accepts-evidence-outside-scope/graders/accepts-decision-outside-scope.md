---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/orders/. The repo's
  `.vibe/decisions/001-order-status-flags.md` (status accepted, outside
  the scope) mandates the four boolean flags of `Order` in
  fixtures/orders/order.py and lists an explicit state machine, a status
  sum type and an event-sourced order among its rejected alternatives; the
  code follows the decision.

  PASS if no `high` or `medium` severity finding proposes a state machine,
  a status enum / sum type, type-state, event sourcing or any other
  lifecycle design for `Order`. A report with no findings at all passes,
  as does a report that names the decision as the reason for staying
  silent.
  FAIL if such a design is proposed for `Order` at high or medium
  severity.
weight: 2
---

Reads the recorded decision that sits outside the path under review and
does not reopen the lifecycle design it settled.

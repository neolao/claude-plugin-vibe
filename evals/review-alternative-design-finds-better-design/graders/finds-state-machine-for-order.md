---
type: llm
focus: last_message
criteria: |
  `Order` in fixtures/orders/order.py tracks its lifecycle with four
  booleans (`is_paid`, `is_shipped`, `is_cancelled`, `is_refunded`) and
  guards each transition by hand; fixtures/api/handlers.py re-derives the
  legal transitions in `can_cancel` and `can_refund`,
  fixtures/api/warehouse_job.py re-derives "shippable", and
  fixtures/ROADMAP.md announces a fifth state (returned). A named design
  makes the illegal combinations unrepresentable and puts the transition
  table in one place.

  PASS if a finding anchored on fixtures/orders/order.py proposes, under
  the `Behaviour over time` or `Type-driven` category (or a clearly
  equivalent label), an explicit state machine, a status sum type /
  type-state, or an equivalent single-source-of-truth lifecycle for
  `Order`, naming the pattern.
  FAIL if no finding proposes such a design for `Order`, or if the finding
  only says the flags are complex without naming the replacement design.
weight: 2
---

Proposes an explicit state machine or a sum type for the boolean-flag
lifecycle whose legal transitions are re-derived in several files and
which is about to grow a fifth state.

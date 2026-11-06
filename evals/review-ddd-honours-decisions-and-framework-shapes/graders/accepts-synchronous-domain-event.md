---
type: llm
focus: last_message
criteria: |
  `PlaceOrder.execute` in fixtures/checkout/place_order.py saves the order
  and then calls `StockReservation.on_order_placed` of
  fixtures/inventory/reservation.py directly with an `OrderPlaced` event
  (fixtures/orders/events.py), in the same request.

  PASS if no `high` or `medium` severity finding claims the event should be
  dispatched asynchronously, through a bus or an outbox, that `OrderPlaced`
  lacks behaviour, or that handling it in the use case is a misalignment. A
  report with no findings at all passes.
  FAIL if the synchronous handling or the event type is flagged for one of
  those reasons at high or medium severity.
weight: 1
---

Does not turn a synchronous domain event into a finding: eventing is a
choice, not a pattern the project has to use.

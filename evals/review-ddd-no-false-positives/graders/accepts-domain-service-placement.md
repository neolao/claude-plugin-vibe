---
type: llm
focus: last_message
criteria: |
  The $500 approval rule lives in `OrderApprovalService` and is orchestrated
  by `CloseOrderUseCase` in fixtures/order_service.py — not in a controller,
  not driven by an HTTP status code.

  PASS if no `high` or `medium` severity Domain isolation finding claims the
  rule sits in the wrong layer.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not misplace a rule that already lives in a domain service.

---
type: llm
focus: last_message
criteria: |
  `OrderRepository.parse_placed_at` delegates to
  `datetime.fromisoformat`, `OrderService` takes its dependencies through
  its constructor with no required call order, and `logging_setup.py` is
  imported and used by `payment_gateway.py`.

  PASS if no `high` or `medium` severity Wheel reinvention, Temporal
  coupling, or Cargo cult finding targets any of the three.
  FAIL if any is flagged at high or medium severity.
weight: 1
---

Does not flag stdlib delegation, constructor injection, or a module that is actually used.

---
type: llm
focus: last_message
criteria: |
  `OrderRow` and `OrderLineRow` in fixtures/orders/persistence.py are the
  table rows the repository reads and writes, beside the `Order` domain type
  of fixtures/orders/order.py which owns the behaviour; the repository
  translates between them and callers only ever receive `Order`s.

  PASS if no `high` or `medium` severity Anemic model, Entity or Repository
  finding claims `OrderRow` / `OrderLineRow` are anemic entities, lack
  identity or behaviour, or leak persistence to the domain. A report with
  no findings at all passes.
  FAIL if one of them is flagged for one of those reasons at high or medium
  severity.
weight: 1
---

Does not call a persistence shape beside the domain type an anemic entity.

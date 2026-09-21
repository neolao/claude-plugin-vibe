---
type: llm
focus: last_message
criteria: |
  The fixtures use only sound DDD patterns:
  - `Order` (fixtures/order.py) is an aggregate root: its invariants
    (max line items, cannot close an empty order) are enforced by its own
    methods (`add_item`, `close`), its `_items`/`_status` are private and
    only exposed as a read-only tuple/property — nothing mutates it from
    outside.
  - `Money` (fixtures/money.py) is an immutable frozen dataclass with
    value-based equality (`add` returns a new instance instead of mutating).
  - `OrderApprovalService`/`CloseOrderUseCase` (fixtures/order_service.py)
    keep the $500 approval business rule in a domain service, orchestrated by
    an application use case — not in a controller/route, and not driven by
    an HTTP status code.
  - `OrderRepository` (fixtures/order_repository.py) is a collection-like
    abstraction (`get`/`save`) that stores and returns domain `Order`
    objects, never raw rows or query strings.
  - Domain vocabulary matches the business (`customer_id`, `Order`, `Money`,
    "approval"), not generic/technical terms.

  PASS if the response reports no `high` or `medium` severity Ubiquitous
  language, Domain isolation, Aggregate, Value object, or Repository finding
  on this code — either no findings at all, or only `low` severity style
  notes unrelated to these already-sound patterns.
  FAIL if it invents a violation on any of the patterns described above (e.g.
  claiming `Order`'s invariants are enforced outside the class, `Money` is
  mutable or compared by identity, the approval rule lives in a
  controller/route, or `OrderRepository` leaks raw rows).
weight: 2
---

Does not invent DDD findings on code that already follows the idiomatic
pattern for each category.

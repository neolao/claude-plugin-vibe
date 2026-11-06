---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/promotions/. `apply_bundle` in
  fixtures/promotions/bundles.py appends straight to `order._lines`, the
  private list of the `Order` aggregate defined outside the scope in
  fixtures/orders/order.py, whose `add_line` enforces the
  1..`MAX_QTY_PER_LINE` (10) quantity rule — the `SUMMER` bundle adds 12.

  PASS if the reported findings include an `Aggregate` (or clearly
  equivalent category name, e.g. "Entity") finding whose FILE: line is
  fixtures/promotions/bundles.py, whose ISSUE names `Order` or
  fixtures/orders/order.py as the aggregate written from outside, and whose
  SUGGESTION names `add_line` as the method to call.
  FAIL if no finding flags the write, if the finding is anchored on
  fixtures/orders/order.py instead of the writer in scope, or if it never
  mentions `add_line`.
weight: 2
---

Anchors the finding on the writer in scope and points at the root's
method: the aggregate sits outside the path under review, the write inside.

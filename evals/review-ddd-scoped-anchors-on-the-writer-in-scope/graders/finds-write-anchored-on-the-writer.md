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
  fixtures/orders/order.py as the aggregate written from outside, which
  names `add_line` somewhere in its ISSUE or SUGGESTION, and whose
  SUGGESTION has `apply_bundle` go through a method of `Order` instead of
  writing `_lines` — `add_line` itself, or a new root method for bundle
  lines (the 12-unit bundle would fail `add_line`'s check, so proposing one
  is sound).
  FAIL if no finding flags the write, if the finding is anchored on
  fixtures/orders/order.py instead of the writer in scope, if it never
  mentions `add_line`, or if its SUGGESTION keeps the write outside `Order`'s
  own methods.
weight: 2
---

Anchors the finding on the writer in scope and points at the root's
method: the aggregate sits outside the path under review, the write inside.

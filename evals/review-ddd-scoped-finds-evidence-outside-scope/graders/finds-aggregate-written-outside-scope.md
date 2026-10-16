---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Aggregate` (or clearly equivalent
  category name, e.g. "Entity") finding about the `Order` aggregate in
  fixtures/orders/order.py whose ISSUE or SUGGESTION names `apply_bundle` in
  fixtures/promotions/bundles.py appending straight to `order._lines`, which
  writes the aggregate's internals from outside and skips `add_line`'s
  1..`MAX_QTY_PER_LINE` (10) quantity check — the `SUMMER` bundle adds 12.
  Whether the finding is anchored on order.py or on bundles.py does not
  matter to this grader.
  FAIL if no finding flags this write, or if the finding never mentions
  fixtures/promotions/bundles.py or `apply_bundle`.
weight: 1
---

Reports the promotion module writing `Order._lines` directly, around the
aggregate's quantity invariant, as an Aggregate finding. Inside the scope the
aggregate is sound: the write is only visible to an agent that greps the
whole repository.

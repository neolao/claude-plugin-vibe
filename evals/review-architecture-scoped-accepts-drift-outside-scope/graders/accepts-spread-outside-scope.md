---
type: llm
focus: last_message
criteria: |
  The glossary's "Promo discount" is computed by `discount_for` in
  fixtures/core/discounts.py and recomputed by `promo_spend` in
  fixtures/reporting/weekly.py — both outside the scope. The in-scope
  fixtures/core/order_service.py only calls `discount_for`.

  PASS if no finding of any severity reports "Promo discount",
  `discount_for` or `promo_spend` as responsibility spread. A report with
  no findings at all passes.
  FAIL if the spread is reported.
weight: 1
---

Leaves a concept spread between two files outside the scope to the full
review.

---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags `quote` in fixtures/shop/shipping_quote.py for
  iterating `cart.lines` — a read of the `Cart` aggregate's read-only
  `lines` property (a tuple copy), not a write to its internals. Findings
  on other files, including an Aggregate finding on promotions.py, do not
  count against this grader, and neither does a report that mentions
  shipping_quote.py only to say it is fine. A finding on shipping_quote.py
  for a reason that has nothing to do with reading `cart.lines` also does
  not count against this grader.
  PASS otherwise.
weight: 1
---

Does not flag the shipping quote for reading the cart's read-only `lines`
view.

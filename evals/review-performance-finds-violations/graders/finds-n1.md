---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `N+1` (or clearly equivalent
  category name) finding on `checkout` in fixtures/checkout_handler.py, for
  calling `db.get_product(...)` inside the loop over `order_lines` — a
  collection that was itself fetched from the database — instead of fetching
  all the needed products in one batched call.
  FAIL if no finding flags this loop as an N+1 query pattern.
weight: 2
---

Reports the per-line `db.get_product` call inside `checkout`'s loop as an
`N+1` finding.

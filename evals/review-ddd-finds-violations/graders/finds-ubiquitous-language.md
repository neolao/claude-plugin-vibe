---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Ubiquitous language` (or clearly
  equivalent category name) finding on `fixtures/order_routes.py`, for naming
  the route parameter and function argument `user_id` when the domain being
  modelled is orders (the checklist's own example: `user` where the domain
  has a word like `customer`).
  FAIL if no finding flags `user_id`/`user` for this reason.
weight: 1
---

Reports the `user_id` naming in `order_routes.py` as a Ubiquitous language
finding.

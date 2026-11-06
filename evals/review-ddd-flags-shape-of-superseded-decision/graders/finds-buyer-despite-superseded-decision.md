---
type: llm
focus: last_message
criteria: |
  fixtures/api/routes.py serves `/buyers/<buyer_id>/orders` and emits
  `buyer_id` for the concept that fixtures/orders/order.py
  (`customer_id`), fixtures/orders/order_repository.py
  (`find_for_customer`) and fixtures/checkout/place_order.py call a
  customer. `.vibe/decisions/001-buyer-kept-in-public-api.md` kept `buyer`
  in the API but is `superseded by 002`, and
  `002-customer-in-public-api.md` (accepted) retires the word.

  PASS if the reported findings include a `Ubiquitous language` (or clearly
  equivalent category name) finding on fixtures/api/routes.py for the
  `buyer` / `customer` split.
  FAIL if no finding flags the split, or if the only reason given for
  staying silent is decision 001.
weight: 2
---

Reports the legacy name: a superseded decision mandates nothing, and the
accepted one retires the word.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Null/absent` (or clearly
  equivalent category name) finding on `checkout_total`
  (fixtures/orders/checkout.py) for reading `quote.amount` while
  `quote_for` (fixtures/shipping/quotes.py) returns `None` for a country
  absent from `CARRIERS`: a checkout with an address outside FR/BE/DE
  raises instead of being refused or quoted. The finding must name
  `quote_for`, fixtures/shipping/quotes.py or the `None` return as the
  evidence.
  FAIL if no finding flags this dereference.
weight: 2
---

Reports the `quote.amount` read in `checkout_total`. checkout.py alone
shows a helper call and an attribute read; only shipping/quotes.py,
outside the scope, shows the helper returns `None`.

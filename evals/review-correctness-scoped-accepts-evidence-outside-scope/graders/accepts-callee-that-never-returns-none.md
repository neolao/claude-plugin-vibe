---
type: llm
focus: last_message
criteria: |
  `checkout_total` in fixtures/orders/checkout.py reads `quote.amount` on
  the result of `quote_for`; `quote_for` in fixtures/shipping/quotes.py
  (outside the scope) returns a `Quote` or raises `UnservedCountry`, never
  `None`, and the `/checkout` handler in fixtures/app/server.py catches
  that exception.

  PASS if no `high` or `medium` severity finding claims `checkout_total`
  dereferences `None`, crashes on an unserved country, or that the
  exception goes unhandled.
  FAIL if it is flagged as a Null/absent issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag an attribute read on a helper that never returns `None`:
checkout.py alone shows a helper call; only shipping/quotes.py, outside
the scope, shows the contract.

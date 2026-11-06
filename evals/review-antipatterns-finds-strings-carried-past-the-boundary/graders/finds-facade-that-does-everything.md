---
type: llm
focus: last_message
criteria: |
  `CheckoutFacade.checkout` in fixtures/checkout/facade.py validates,
  prices, charges, records the shipment and sends the receipt email
  itself, with SQL and SMTP inline; it delegates nothing.

  PASS if the reported findings include a `God object` / `God function`
  (or clearly equivalent category name) finding on `CheckoutFacade` or
  `CheckoutFacade.checkout`.
  FAIL if no finding flags `CheckoutFacade` for doing every step itself.
weight: 2
---

Reports the class named "Facade" as a God object: the name does not make a
facade, delegating does.

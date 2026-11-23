---
type: llm
focus: last_message
criteria: |
  In fixtures/orders/service.py, `OrderService.__init__` receives its
  `repository` as a parameter but still builds its payment gateway by hand
  (`self.payments = PaymentGateway(settings.PAYMENT_URL)`).

  PASS if the reported findings include a finding anchored on
  fixtures/orders/service.py, in the `Half-done migration` category (or a
  clearly equivalent name), that says the gateway is built by hand while the
  repository is received as a parameter, and suggests receiving the gateway
  as a parameter too.
  FAIL if no finding flags the hand-built gateway of `OrderService`, or if the
  finding never contrasts it with the injected repository.
weight: 1
---

Reports `OrderService` getting one collaborator by injection and its sibling
collaborator by hand-construction, in the same constructor.

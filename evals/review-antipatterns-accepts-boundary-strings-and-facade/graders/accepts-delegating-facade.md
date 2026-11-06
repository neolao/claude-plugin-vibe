---
type: llm
focus: last_message
criteria: |
  `CheckoutFacade.checkout` in fixtures/checkout/facade.py performs none
  of the five steps itself: each is one call to an injected collaborator
  from fixtures/checkout/collaborators.py.

  PASS if no `high` or `medium` severity God object / God function (or
  equivalent) finding targets `CheckoutFacade`. A report with no findings
  at all passes.
  FAIL if `CheckoutFacade` is flagged at high or medium severity as a
  god object.
weight: 1
---

Does not call a coordinator that only delegates a god object.

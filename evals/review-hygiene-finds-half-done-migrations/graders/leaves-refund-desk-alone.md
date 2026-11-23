---
type: llm
focus: last_message
criteria: |
  In fixtures/support/refunds.py, `RefundDesk.__init__` builds its own
  `PaymentGateway(settings.PAYMENT_URL)` and receives nothing as a
  parameter: no new mechanism was adopted in that unit.

  Only a finding counts: a block with a `FILE:` line. A finding anchored
  elsewhere (for example on fixtures/orders/service.py) that mentions
  `RefundDesk` in its ISSUE or SUGGESTION passes, and so does a sentence
  outside any finding.
  PASS if no finding is anchored (its `FILE:` line) on
  fixtures/support/refunds.py.
  FAIL if a finding is anchored on fixtures/support/refunds.py, for example
  asking for its gateway to be injected.
weight: 1
---

Does not sweep the old mechanism in a unit that never adopted the new one:
a half-done migration is judged inside one unit.

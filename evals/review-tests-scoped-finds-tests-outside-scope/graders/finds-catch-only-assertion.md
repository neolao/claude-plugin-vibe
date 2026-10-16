---
type: llm
focus: last_message
criteria: |
  PASS if a finding targets "rejects an unknown customer" in
  fixtures/tests/invoice.test.js and says that its only assertion sits
  inside the `catch` block, so if `billingAddress` stopped throwing for an
  unknown customer nothing would run and the test would still pass. Any
  category fits (`Tautological`, `Under-asserting`, `Missing negative
  cases`...) as long as the finding names the catch-only assertion (or
  the missing `assert.rejects` / fail-if-no-throw guard).
  FAIL if no finding points out that this negative test passes when no
  error is thrown.
weight: 1
---

Reports the negative test whose assertion is only reached inside `catch`:
a regression that stops throwing leaves it green.

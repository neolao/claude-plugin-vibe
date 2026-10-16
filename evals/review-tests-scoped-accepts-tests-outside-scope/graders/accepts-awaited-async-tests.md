---
type: llm
focus: last_message
criteria: |
  In fixtures/tests/invoice.test.js, "resolves the billing address" awaits
  `billingAddress(...)` before asserting the literal address, and "rejects
  an unknown customer" awaits `assert.rejects(...)`: both assertions run
  inside the test and fail it on a wrong result.

  PASS if no `high` or `medium` severity Tautological, Under-asserting or
  Over-mocked finding targets either of these two tests. A report with no
  findings at all passes.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not call an awaited async assertion vacuous, nor a one-method stub of
the directory over-mocking when the assertion checks the code's own
result.

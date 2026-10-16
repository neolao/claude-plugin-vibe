---
type: llm
focus: last_message
criteria: |
  PASS if a finding targets "resolves the billing address" in
  fixtures/tests/invoice.test.js and says that the promise carrying the
  `assert.equal` (the `.then(...)` chain) is neither awaited nor returned,
  so the test is reported as passing whatever the resolved address is.
  Any category fits (`Tautological`, `Under-asserting`, `Async`...) as
  long as the finding names the unawaited / unreturned promise.
  FAIL if no finding points out that this test's assertion runs outside
  the test, after it has already passed.
weight: 2
---

Reports the assertion behind an unawaited, unreturned promise: the test
passes before its only assertion runs. `review-robustness` skips test
files, so no other agent sees it.

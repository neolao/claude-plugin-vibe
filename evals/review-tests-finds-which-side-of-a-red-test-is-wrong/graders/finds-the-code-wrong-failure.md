---
type: llm
focus: last_message
criteria: |
  `test_fee_is_capped_at_five` in fixtures/test_fees.py expects
  `transfer_fee(1000)` to be `5.0`, the cap fixtures/README.md states
  ("never more than 5.00"); `transfer_fee` in fixtures/fees.py returns
  `round(amount * 0.02, 2)` with no cap, so the run gets 20.0. The test
  is right and the code is wrong.

  PASS if a `Failing test` (or clearly equivalent category name, such as
  `Failing`, `Red test` or `Coverage gap` when it reports this failure)
  finding is anchored (its FILE: line) on fixtures/test_fees.py and its
  ISSUE says the code is wrong — the cap is missing, the README's rule is
  not applied — not the test.
  FAIL if no finding reports this failure, if the finding says the test's
  expectation of 5.0 is wrong or should be changed to 20.0, or if the
  finding is anchored on fixtures/fees.py without naming the test.
weight: 2
---

Reports the failure the code causes as a Failing test on the test, and
says the code, not the test, is the wrong side.

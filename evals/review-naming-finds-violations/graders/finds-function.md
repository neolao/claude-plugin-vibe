---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Function` (or clearly equivalent
  category name) finding on at least one of:
  - `OrderProcessor.calc` in fixtures/order_processor.py, for an abbreviated name
    that hides its intent (calculating a discounted total), or
  - `UserManager.process` in fixtures/userManager.py, for a generic name that
    hides its second responsibility (it validates the user AND writes the
    payload to disk), or
  - `UserManager.checkUser` in fixtures/userManager.py, for a boolean-returning
    method not phrased as a question (should read like `is_user_active`).
  Any one of these three is enough to pass.
  FAIL if none of them is flagged as a Function naming issue.
weight: 2
---

Reports at least one of `calc`, `process`, or `checkUser` as a `Function`
finding.

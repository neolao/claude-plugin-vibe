---
type: llm
focus: last_message
criteria: |
  Criterion 2 asks the email to give the product name and the remaining
  quantity. `build_message` in fixtures/notify.py only writes the product
  name.

  PASS if a `(gap)` finding quotes criterion 2 (or its wording) and says the
  remaining quantity is missing from the email, with a fix (add the quantity
  to the message).
  FAIL if the missing quantity is not reported as a gap.
weight: 2
---

A criterion met in part is an uncovered requirement for its missing part.

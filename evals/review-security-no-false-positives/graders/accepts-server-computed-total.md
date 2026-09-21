---
type: llm
focus: last_message
criteria: |
  `charge_for_order` takes only the SKUs and quantities from the uploaded
  file and computes the amount from `CATALOGUE`, so no number in the file
  reaches the payment call.

  PASS if no finding claims the charged amount comes from untrusted input or
  needs validating.
  FAIL if it is flagged as a Trust boundary or unvalidated-input issue.
weight: 1
---

Does not flag the server-computed total as untrusted input.

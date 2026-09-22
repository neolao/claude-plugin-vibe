---
type: llm
focus: last_message
criteria: |
  `charge_for_order` validates each line's `quantity` (must be an int in
  `(0, MAX_LINE_QUANTITY]`) before multiplying it into the total, so a
  malicious or malformed quantity is rejected before it can reach the
  payment call.

  PASS if no finding claims the charged amount comes from untrusted input or
  needs validating.
  FAIL if it is flagged as a Trust boundary or unvalidated-input issue.
weight: 1
---

Does not flag the server-computed total as untrusted input.

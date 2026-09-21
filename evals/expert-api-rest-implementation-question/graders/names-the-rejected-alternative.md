---
type: llm
focus: last_message
criteria: |
  PASS if the reply names the alternative it turned down (for example the
  other status code it considered) and says why it loses here.
  FAIL if only the recommendation appears, with no rejected option.
weight: 2
---

Names the rejected alternative, as the implementation-time format requires.

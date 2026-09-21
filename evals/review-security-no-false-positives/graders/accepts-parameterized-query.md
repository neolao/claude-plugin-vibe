---
type: llm
focus: last_message
criteria: |
  The SQL call passes user input through a `?` placeholder, never string
  concatenation or interpolation.

  PASS if no `high` or `medium` severity Injection finding claims SQL
  injection here.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a parameterized query SQL injection.

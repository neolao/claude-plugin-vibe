---
type: llm
focus: last_message
criteria: |
  `is_active` is already phrased as the question a boolean should answer.

  PASS if no `high` or `medium` severity Function finding says it should be
  renamed to read as a question, or that its name overpromises.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not ask an already-interrogative boolean name to be rephrased.

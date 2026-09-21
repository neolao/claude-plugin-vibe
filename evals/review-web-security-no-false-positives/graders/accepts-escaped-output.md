---
type: llm
focus: last_message
criteria: |
  `search` passes `q` through `markupsafe.escape` before embedding it in the
  HTML response.

  PASS if no `high` or `medium` severity XSS finding targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call escaped output XSS.

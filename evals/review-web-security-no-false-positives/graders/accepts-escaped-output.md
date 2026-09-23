---
type: llm
focus: last_message
criteria: |
  `search` passes `q` through `markupsafe.escape` before embedding it in the
  HTML response.

  PASS if no `high` or `medium` severity XSS finding targets it. A report
  with no findings at all passes, and so does one that does not mention it.
  FAIL only if it is flagged at high or medium severity.
weight: 1
---

Does not call escaped output XSS.

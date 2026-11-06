---
type: llm
focus: last_message
criteria: |
  The agent's definition says a working design never blocks: an
  alternative-design finding is `medium` at most.

  PASS if no finding in the report has `SEVERITY: high` (bold or plain
  label).
  FAIL if any finding is reported at high severity.
weight: 1
---

A working design never blocks: no alternative-design finding is high.

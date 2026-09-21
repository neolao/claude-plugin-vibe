---
type: llm
focus: last_message
criteria: |
  Channel senders are looked up in a `NOTIFIERS` registry; adding a channel
  means adding an entry, not editing a branch chain.

  PASS if no `high` or `medium` severity `O` finding claims this must be
  edited to extend.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call registry-based dispatch an OCP violation.

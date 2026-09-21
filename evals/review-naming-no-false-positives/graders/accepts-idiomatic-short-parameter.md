---
type: llm
focus: last_message
criteria: |
  The single-letter `e` parameter for an event in `EventBus.publish` is the
  checklist's own example of a short name that is idiomatic in its context.

  PASS if no `high` or `medium` severity Variable finding calls `e` cryptic
  or demands it be spelled out.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call the checklist's own idiomatic short name cryptic.

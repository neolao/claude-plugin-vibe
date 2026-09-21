---
type: llm
focus: last_message
criteria: |
  `express` is pinned to the exact, current `4.19.2`. An exact pin is a
  legitimate choice, not the `*`/`latest`/`>=x` shape the checklist flags.

  PASS if no `high` or `medium` severity Version hygiene finding targets
  this pin.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call an exact version pin a version-hygiene problem.

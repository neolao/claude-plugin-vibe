---
type: llm
focus: last_message
criteria: |
  `UserContact` is a two-field dataclass and `format_greeting` reads both
  fields — no client depends on a member it does not use.

  PASS if no `high` or `medium` severity `I` finding claims a fat interface
  or unused members here.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not invent an ISP violation on a dataclass whose fields are all used.

---
type: llm
focus: last_message
criteria: |
  Finding 4 (VIP customers get 20% per the brief; the module never reads a
  `vip` flag): the deliverable ignores a requirement outright — the need was
  not framed into the code at all.

  PASS if that finding is kept and routed to the `need` space (written
  `(<level> · need)` or equivalent wording), at level `high` or `medium`.
  FAIL if it is routed to `implementation`, dropped, or kept as `low`.
weight: 2
---

A requirement the code does not know about sends the loop back to the need
framing, not to the implementation.

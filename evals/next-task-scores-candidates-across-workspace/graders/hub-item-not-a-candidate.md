---
type: llm
focus: last_message
criteria: |
  The hub repo has its own `todo` item, 001 "Decide The Shared Error
  Envelope". Step 3 says the hub's own items are never candidates — they are
  workspace decisions, not implementable work.

  PASS if the hub item is not presented as a candidate or a runner-up (it may
  be mentioned as a decision the workspace still owes).
  FAIL if it is offered as work to pick up.
weight: 1
---

Keeps the hub's own item out of the candidate list.

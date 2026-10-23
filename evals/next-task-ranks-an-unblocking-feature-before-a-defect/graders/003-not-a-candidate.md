---
type: llm
focus: last_message
criteria: |
  Item 003 depends on 001, which is still `todo`: it is not eligible.

  PASS if the presentation does not offer item 003 as the pick or as a
  runner-up (it may name it as the item 001 unblocks).
  FAIL if item 003 is presented as a candidate.
weight: 1
---

An item with an unmet dependency is never a candidate.

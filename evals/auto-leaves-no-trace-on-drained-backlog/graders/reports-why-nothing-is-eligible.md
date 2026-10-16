---
type: llm
focus: last_message
criteria: |
  The backlog holds two active items: 003 is `blocked` (possible duplicate of
  002) and 004 depends on 003. Nothing is eligible, so the run has nothing to
  do.

  PASS if the final message says no item was eligible (or equivalent: nothing
  to do, backlog drained) and gives the reason — 003 blocked and/or 004
  waiting on 003 — without claiming to have started, shipped, or blocked an
  item, or to have opened and closed a run with a commit.
  FAIL if it reports starting or shipping 004 or 003, says a run was opened
  or closed with a commit, blames a turn limit, a timeout or an error, or
  gives no reason at all.
weight: 2
---

Says why nothing happened, instead of pretending a run took place.

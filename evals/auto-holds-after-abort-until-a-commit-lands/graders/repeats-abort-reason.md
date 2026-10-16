---
type: llm
focus: last_message
criteria: |
  The journal says the last run aborted because the build is broken
  (`python3 -m compileall -q .` fails on listutils.py). HEAD is still that
  run's closing commit and the working tree is clean, so nothing has been
  fixed since.

  PASS if the final message says the previous run aborted on the broken
  build (or an equivalent wording about the build/compile failing), says
  that nothing has changed since (no new commit, clean tree, or equivalent),
  and makes clear that no item was started.
  FAIL if it reports starting, shipping or blocking 003 or 004, says a new
  run was opened or closed, claims to have repaired the build, or gives no
  reason for doing nothing.
weight: 2
---

Repeats the journaled abort reason and says nothing changed, instead of
re-running the item into the same wall.

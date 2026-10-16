---
type: llm
focus: last_message
criteria: |
  A commit repaired the build after the aborted run closed, so the skill must
  have started a new run rather than holding.

  PASS if the final message shows 003 as shipped (done) in its summary table
  or status lines and gives the limit being reached as the reason the run
  stopped.
  FAIL if it says nothing changed since the abort and that no item was
  started, reports 003 as aborted or blocked, or blames a turn limit, a
  timeout or an error.
weight: 1
---

Does not mistake a repaired build for an untouched one.

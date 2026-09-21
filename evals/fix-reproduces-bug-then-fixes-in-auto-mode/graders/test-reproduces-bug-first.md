---
type: llm
focus: last_message
criteria: |
  skills/fix/SKILL.md's Steps 3-5 require: "The first test reproduces the bug
  exactly: it fails on the current code, proving the bug exists, and
  describes the correct behaviour ... A test that passes before the fix does
  not reproduce the bug — revise it." Step 9's report must state "the test
  that now covers the bug".

  PASS if the final report's red/green narrative shows the reproducing test
  (asserting `max([-5, -2, -9])` equals `-2`, or an equivalent all-negative
  case) was written and confirmed to FAIL against the buggy code before any
  fix was applied — i.e. red-then-green, test-first.

  FAIL if the narrative suggests the test was written after or alongside the
  fix (no red step reported), or if no test for the all-negative case is
  mentioned at all.

  This is a narrative-level check on the report, not a read of the actual
  tool-call order, since exact ordering may not be cheaply gradable — see
  the eval's caveats on this axis.
weight: 2
---

Confirms, from the reported narrative, that the reproducing test came before
the fix (red before green), not after.

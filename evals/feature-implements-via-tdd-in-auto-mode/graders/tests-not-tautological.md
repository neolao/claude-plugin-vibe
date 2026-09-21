---
type: llm
focus: last_message
criteria: |
  workflow.md's Red step forbids tautological tests: "an expected value
  derived with the same computation as the code under test", "trivially true
  assertions", or "assertions unrelated to the behaviour claimed".

  PASS if nothing in the final report's description of the new tests reveals
  a tautological test for `sum` — e.g. computing the expected sum with the
  same reduce/loop logic as the implementation instead of a pinned literal,
  or asserting something unrelated to the summed value (like "did not
  throw") for the nominal case.

  This is a narrative-level check on the report, not a read of the actual
  test file, so it can only catch a tautology the agent's own report
  surfaces or fails to hide (see the eval's caveats on this axis) — default
  to PASS when the report gives no reason to suspect a tautology.
weight: 1
---

Spot-checks, from the reported narrative, that the new tests are not
tautological (a subtly wrong implementation could still pass them).

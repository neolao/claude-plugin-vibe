---
type: llm
focus: trace
criteria: |
  Look at the `TaskCreate` and `TaskUpdate` calls made after the deletions
  of the return to planning.

  PASS if five new tasks were created through `TaskCreate`, with subjects
  "Round 2 — Plan", "Round 2 — Implement", "Round 2 — Review",
  "Round 2 — Document" and "Round 2 — Commit" (an ASCII hyphen in place of
  the dash is acceptable), and each of the last four was made blocked by
  the previous one (through `addBlockedBy` on a `TaskUpdate`, or the
  equivalent field at creation).
  FAIL if fewer than five tasks were created, if a subject lacks the
  `Round 2` prefix, if the dependency chain is missing or wrong, or if the
  first round's tasks were reused or renamed instead of new ones created.
weight: 1
---

The new round is a fresh chain of five prefixed tasks, created next to the
first round's completed ones.

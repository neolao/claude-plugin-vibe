---
type: llm
focus: last_message
criteria: |
  Finding 1 is true: fixtures/export.py:12 indexes three keys with no guard,
  and an incomplete row aborts the whole export.

  PASS if finding 1 is kept under `## CLASSIFIED findings`, in the
  `implementation` space, at level `high` or `medium`, with a concrete
  **Consequence:** sentence.
  FAIL if it is dropped, merged away, routed to `need`, or kept as `low`.
weight: 2
---

A valid finding is kept, not second-guessed into oblivion.

---
type: llm
focus: last_message
criteria: |
  The kept finding on the offset defect (`start = page * PAGE_SIZE` at
  handlers.py:14) is a real bug: page 1 returns the second page, and the
  need (pages starting at 1) is understood by the code, which tries to meet
  it and gets the offset wrong.

  PASS if that finding is kept under `## CLASSIFIED findings` at level
  `high` and in the `implementation` space, with a concrete **Consequence:**
  sentence.
  FAIL if it is any other level or space, or not kept.
weight: 2
---

Level by the consequence, space by whether the need was understood.

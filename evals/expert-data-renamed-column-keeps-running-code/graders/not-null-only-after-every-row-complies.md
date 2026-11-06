---
type: llm
focus: last_message
criteria: |
  Roughly a third of the two million `users` rows have no phone number at
  all. A migration that adds `NOT NULL` on the new column before those
  rows hold a value fails outright, or succeeds only by locking the table
  while it rewrites every row. The expert's checklist says a column gets
  `NOT NULL` only once every existing row satisfies it.

  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says the new column stays
  nullable (or gets `NOT NULL` only in a later step) until the rows with
  no phone have been handled — a batched backfill of the existing numbers
  plus a decision on the rows that have none (a placeholder, a default,
  or the constraint left off until the product says what those users must
  do) — and that the backfill of two million rows runs in batches rather
  than one statement.
  FAIL if the reply adds `NOT NULL` in the migration that creates or
  renames the column with no word on the rows that have no phone, or runs
  the backfill as one update of the whole table.
weight: 2
---

Puts the `NOT NULL` after the backfill and the handling of the third of
rows with no phone, with the backfill batched — never a constraint the
existing rows cannot satisfy.

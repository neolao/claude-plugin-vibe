---
type: llm
focus: last_message
criteria: |
  The brief adds one nullable column and one new table and changes
  nothing that exists: every column the running code reads and writes
  stays as it is, and the new column is empty until a user fills it. The
  expert's own checklist says a new nullable column or a new table needs
  no expand/contract sequence.

  PASS if no REQUIREMENTS entry demands a multi-release sequence, a
  dual-write period, a transitional column, a feature flag on the schema,
  a batched backfill of the existing rows, or a notice to the sales team as
  a condition of this change. Stating that the previous version keeps
  working during the rollout because it ignores the new column and table,
  with a test scenario for it, is expected and passes; a RISKS entry on
  adding the column with a non-null default on a large table, or a
  requirement that the migration not lock `users`, also passes.
  FAIL if REQUIREMENTS requires a dual-write period, a transitional column,
  a multi-release expand/contract sequence or a backfill of the two
  million rows as the condition for adding `timezone` or
  `user_preferences`.
weight: 2
---

Does not reach for an expand/contract sequence on an additive change: the
compatibility rule triggers on what the running code would feel, and here
it feels nothing.

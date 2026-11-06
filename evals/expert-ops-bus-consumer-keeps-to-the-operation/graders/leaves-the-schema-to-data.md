---
type: llm
focus: last_message
criteria: |
  The brief says the data team is designing the `invoice_archive` table's
  columns, constraints and indexes alongside this change. The expert's
  scope sentence keeps the consumer's operation here and routes the schema
  a job touches to `expert-data`.

  PASS if no REQUIREMENTS entry prescribes the table's column types, its
  primary key, its constraints or its indexes. Mentioning them in passing
  as another expert's domain, naming `expert-data`, or requiring that the
  write be idempotent on the invoice id (a uniqueness the consumer relies
  on, however the table enforces it), all pass: what the consumer relies
  on is the operation's, how the table provides it is the schema's.
  FAIL if REQUIREMENTS prescribes the column types, the primary key, a
  specific index or a retention mechanism inside the table, as if the
  expert owned the schema.
weight: 1
---

Keeps the column types, the constraints and the index out of its
REQUIREMENTS: the consumer's operation is its domain, the archive table's
shape is `expert-data`'s.

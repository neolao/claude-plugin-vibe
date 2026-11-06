---
type: llm
focus: last_message
criteria: |
  `Order` in fixtures/shop/models.py is a Django model: its columns
  (`customer_email`, `status`, `total_cents`, `currency`) must be the
  field types the ORM maps to the database.

  PASS if no `high` or `medium` severity Primitive obsession or
  Stringly-typed (or equivalent) finding targets the column declarations
  of `Order`. A report with no findings at all passes.
  FAIL if a column declaration of `Order` is flagged at high or medium
  severity for being a bare string or integer.
weight: 1
---

Does not call an ORM model's column declarations primitive obsession.

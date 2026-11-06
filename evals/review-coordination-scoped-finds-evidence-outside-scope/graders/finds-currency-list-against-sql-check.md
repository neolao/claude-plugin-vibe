---
type: llm
focus: last_message
criteria: |
  fixtures/api/handlers.py defines `ALLOWED_CURRENCIES = ("EUR", "USD",
  "GBP")` and validates payloads against it; fixtures/db/schema.sql,
  outside the scope, restates the same three codes in `CHECK (currency IN
  ('EUR', 'USD', 'GBP'))`. Nothing generates one from the other, no test
  compares them.

  PASS if the reported findings include a finding anchored (its FILE: line)
  on fixtures/api/handlers.py, in category `Duplicated case list` (or a
  clearly equivalent name), whose ISSUE or SUGGESTION names
  fixtures/db/schema.sql or the SQL CHECK as the other copy.
  FAIL if no finding names the two copies of the currency list, or if the
  finding never points at the SQL side.
weight: 2
---

Reports the currency list against its SQL copy, anchored on the in-scope
handler: the second expression lives in another language and outside the
scope, and only an agent that greps the whole repository finds it.

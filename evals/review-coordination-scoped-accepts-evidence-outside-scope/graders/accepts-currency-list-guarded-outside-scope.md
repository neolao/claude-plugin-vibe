---
type: llm
focus: last_message
criteria: |
  fixtures/api/handlers.py imports `ALLOWED_CURRENCIES` from
  fixtures/core/currencies.py. fixtures/db/schema.sql restates the three
  codes in a SQL CHECK, and fixtures/tests/test_schema.py — outside the
  scope — reads the schema, extracts the CHECK's codes and asserts they
  equal `ALLOWED_CURRENCIES`: changing either side fails the suite.

  PASS if no `high` or `medium` severity finding names the currency list,
  `ALLOWED_CURRENCIES`, `validate_invoice` or the SQL CHECK as a
  duplicated case list or any coordination to maintain. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if the currency list is flagged at high or medium severity.
weight: 2
---

Keeps a copy whose guard sits outside the scope: the test comparing the
SQL CHECK with the shared definition is in a file the agent was not given,
so a verdict reached from fixtures/api/ alone would be a guess.

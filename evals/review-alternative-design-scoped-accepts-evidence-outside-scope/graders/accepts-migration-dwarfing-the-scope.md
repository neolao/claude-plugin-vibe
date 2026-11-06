---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/orders/ (two files). `OrderReport` in
  fixtures/orders/report.py takes seven positional arguments; its twelve
  call sites live in six files outside the scope (fixtures/api/
  account_page.py, support_console.py, invoice_endpoint.py; fixtures/jobs/
  monthly_statement.py, daily_digest.py, tax_export.py). Any design that
  changes how a report is built (a Builder, a parameter object, keyword
  construction, a factory) moves those six files too: a seven-file
  migration for a one-file unit in a two-file scope, which the agent's
  definition calls `WORSE` whatever the design's merits.

  PASS if no `high` or `medium` severity finding proposes a Builder, a
  parameter object, a fluent constructor or any other construction design
  for `OrderReport`. A report with no findings at all passes, as does a
  finding dropped with its migration count as the reason.
  FAIL if such a design is proposed for `OrderReport` at high or medium
  severity.
weight: 2
---

Counts the callers outside the scope into the migration and drops a
proposal whose migration dwarfs the scope.

---
type: llm
focus: last_message
criteria: |
  Two defects sit entirely outside the scope: the `reporting` module
  (fixtures/reporting/weekly.py) is imported by nothing and is not an
  entry point, and fixtures/adapters/postgres_gateway.py calls
  `SmtpNotifier()` directly, adapter to adapter. No in-scope file takes
  part in either.

  PASS if no finding of any severity reports `reporting` as an orphaned
  module and no finding reports the `SmtpNotifier` call of
  fixtures/adapters/postgres_gateway.py as adapter purity (or any other
  category).
  FAIL if either is reported.
weight: 1
---

Leaves drift no in-scope file takes part in to the full review.

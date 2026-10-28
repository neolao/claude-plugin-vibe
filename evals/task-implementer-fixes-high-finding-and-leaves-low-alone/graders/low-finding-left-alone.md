---
type: llm
focus: last_message
criteria: |
  The `low` finding is only about the name `lvl` in `is_low`, a method the `high` finding does not concern. The agent's
  definition says a `low` finding is not its to fix unless the caller says
  so; the prompt does not say so.

  PASS if the `inventory/stock.py` content the workflow observed still
  names that variable `lvl` in `is_low` (or the agent's own edit left that
  name untouched).
  FAIL if the variable was renamed.
weight: 2
---

A `low` finding is not widened into the correction.

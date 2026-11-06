---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/orders/. Files outside it
  (fixtures/shipping/, fixtures/catalog/, fixtures/inventory/,
  fixtures/reports/, fixtures/app/) may be named inside a finding's ISSUE,
  SCENARIO or SUGGESTION as the evidence or as the other end of the bug.

  PASS if every finding's FILE: line points to a file under
  fixtures/orders/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/orders/, for example a finding on fixtures/reports/summary.py,
  fixtures/catalog/sku.py or fixtures/shipping/quotes.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on.

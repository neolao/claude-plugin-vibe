---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/orders/. Files outside it
  (fixtures/api/, fixtures/jobs/, `.vibe/`) may be named inside a
  finding as evidence.

  PASS if every finding's FILE: line points to a file under
  fixtures/orders/, or if there is no finding at all.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/orders/, for example a finding on fixtures/api/invoice_endpoint.py
  or fixtures/jobs/tax_export.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope, or stays silent.

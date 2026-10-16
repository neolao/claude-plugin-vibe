---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/orders/. Files outside it
  (fixtures/customers/, fixtures/promotions/, fixtures/checkout/,
  fixtures/shipping/, fixtures/dunning/, fixtures/api/) may be named inside
  a finding's ISSUE or SUGGESTION as the evidence or as the other side of
  the boundary.

  PASS if every finding's FILE: line points to a file under fixtures/orders/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/orders/, for example a finding on fixtures/promotions/bundles.py
  or fixtures/customers/address.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on.

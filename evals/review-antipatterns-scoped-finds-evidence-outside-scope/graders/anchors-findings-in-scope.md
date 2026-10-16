---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/orders/. Files outside it
  (fixtures/campaigns/, fixtures/invoicing/, fixtures/notifications/,
  fixtures/requirements.txt) may be named inside a finding's ISSUE or
  SUGGESTION as evidence.

  PASS if every finding's FILE: line points to a file under fixtures/orders/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/orders/, for example a finding on fixtures/campaigns/admin.py or
  fixtures/notifications/email.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on.

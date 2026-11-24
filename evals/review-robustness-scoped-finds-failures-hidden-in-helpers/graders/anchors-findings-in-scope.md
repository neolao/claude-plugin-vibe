---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/billing/. Files outside it
  (fixtures/db/, fixtures/net/, fixtures/common/, fixtures/gateway/, fixtures/locks/)
  may be named inside a finding's ISSUE or SUGGESTION as the evidence or as
  the other end of the failure path.

  PASS if every finding's FILE: line points to a file under fixtures/billing/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/billing/, for example a finding on fixtures/db/tx.py or
  fixtures/net/retry.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on.

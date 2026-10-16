---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/shipping/. Files outside it
  (fixtures/carriers/, fixtures/events/, fixtures/spool/, fixtures/workers/)
  may be named inside a finding's ISSUE or SUGGESTION as the evidence or as
  the other end of the failure path.

  PASS if every finding's FILE: line points to a file under fixtures/shipping/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/shipping/, for example a finding on fixtures/carriers/http.py or
  fixtures/workers/close_day.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on.

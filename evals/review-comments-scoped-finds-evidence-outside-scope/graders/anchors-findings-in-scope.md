---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/sync/. Files outside it
  (fixtures/config/settings.py, fixtures/gateway/client.py) may be named
  inside a finding's ISSUE or SUGGESTION as evidence.

  PASS if every finding's FILE: line points to a file under fixtures/sync/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/sync/ — for example a finding on the `# maximum number of
  attempts` comment of fixtures/config/settings.py in its own right.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on — the redundant
comment of fixtures/config/settings.py is outside the scope and is never a
finding here.

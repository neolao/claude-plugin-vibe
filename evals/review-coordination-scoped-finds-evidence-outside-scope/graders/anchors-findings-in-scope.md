---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/api/. Files outside it
  (fixtures/db/schema.sql, fixtures/jobs/archive.py,
  fixtures/jobs/retention.py, fixtures/web/settings_page.py) may be named
  inside a finding's ISSUE or SUGGESTION as evidence. The retention period
  is written as `RETENTION_DAYS = 90` in fixtures/jobs/retention.py and as
  "kept for 90 days" in fixtures/web/settings_page.py, both outside the
  scope.

  PASS if every finding's FILE: line points to a file under fixtures/api/.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/api/ — for example a finding on the retention period, whose two
  copies both sit outside the scope.
weight: 1
---

Keeps every finding anchored on a file in scope: the whole repository is
read for evidence, but only the path given is reported on — a coordination
whose two copies both sit outside the scope is never a finding here.

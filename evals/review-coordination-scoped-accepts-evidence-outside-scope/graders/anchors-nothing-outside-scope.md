---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/api/. The retention period is
  written as `RETENTION_DAYS = 90` in fixtures/jobs/retention.py and as
  "kept for 90 days" in fixtures/web/settings_page.py, both outside the
  scope, with nothing keeping them aligned.

  PASS if no finding's FILE: line points to a file outside fixtures/api/ —
  a report with no findings at all passes, and so does a finding on
  fixtures/api/handlers.py that merely mentions an outside file as
  evidence.
  FAIL if any finding is anchored (its FILE: line) on
  fixtures/jobs/retention.py, fixtures/web/settings_page.py,
  fixtures/db/schema.sql, fixtures/core/currencies.py,
  fixtures/core/filenames.py or fixtures/jobs/archive.py.
weight: 2
---

Reports nothing on a coordination whose two copies both sit outside the
scope, however unguarded: the scope bounds what is reported, not what is
read.

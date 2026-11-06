---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/sync/. The files outside it
  carry comments that repeat their code: `# maximum number of attempts` and
  `# the poll delay` in fixtures/config/settings.py, `# open the gateway
  url` in fixtures/gateway/client.py.

  PASS if no finding's FILE: line points to a file outside fixtures/sync/ —
  a report with no findings at all passes, and so does a finding on
  fixtures/sync/poller.py that merely mentions an outside file as evidence.
  FAIL if any finding is anchored (its FILE: line) on
  fixtures/config/settings.py, fixtures/gateway/client.py or
  fixtures/workers/scheduler.py.
weight: 1
---

Reports nothing on the comments outside the scope, however redundant: the
scope bounds what is reported, not what is read.

---
type: llm
focus: last_message
criteria: |
  fixtures/sync/poller.py reads `batch = fetch_pending()  # raises on HTTP
  error: the scheduler logs it and retries next period`. Both halves are
  true, and only of files outside the scope: `fetch_pending` in
  fixtures/gateway/client.py raises `RuntimeError` on a 4xx/5xx status, and
  `run_forever` in fixtures/workers/scheduler.py catches it, logs a warning
  and sleeps until the next period.

  PASS if no `high` or `medium` severity finding calls that comment
  misleading or redundant, or asks to delete it. A `low` finding passes, as
  does a report with no findings at all.
  FAIL if the comment is flagged at high or medium severity as Misleading,
  Redundant (or equivalent), or if a finding at any severity suggests
  deleting it.
weight: 1
---

Keeps a comment whose truth is only visible outside the scope: the raise and
the catch both sit in files the agent was not given, so a verdict reached
from fixtures/sync/ alone would be a guess.

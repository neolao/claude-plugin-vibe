---
type: llm
focus: last_message
criteria: |
  `complete_order` in fixtures/webhook_dispatcher.py creates a task the way
  an unawaited fire-and-forget call would, but its docstring marks the call
  as intentionally fire-and-forget, `notify_partner` catches and logs its
  own failure with the order id, and `add_done_callback` retrieves the
  exception so nothing is lost or warns at exit.

  PASS if no `high` or `medium` severity finding claims this task is
  unawaited, untracked, or a silent-failure risk.
  FAIL if it is flagged as an Async issue (or equivalent) at high or medium
  severity.
weight: 1
---

Does not flag the explicitly marked, self-handling fire-and-forget task.

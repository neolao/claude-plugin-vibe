---
type: llm
focus: last_message
criteria: |
  `record_payment` in fixtures/billing/audit.py creates a task for
  `append_audit_line` without awaiting it; its docstring marks the call as
  intentionally fire-and-forget, the task's result is never read, the
  task is held in `_pending` until done, and `append_audit_line` bounds
  and logs its own failure.

  PASS if no `high` or `medium` severity finding claims `record_payment`
  misses an `await`, returns before the audit line is written as a bug,
  or uses the task's result wrongly.
  FAIL if it is flagged as a missing-await or wrong-result issue at high
  or medium severity.
weight: 1
---

Does not flag an explicitly marked fire-and-forget whose result nothing
reads: a silent failure there would be review-robustness's subject, and
this one handles its own.

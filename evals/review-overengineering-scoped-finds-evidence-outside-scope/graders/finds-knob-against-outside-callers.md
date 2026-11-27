---
type: llm
focus: last_message
criteria: |
  fixtures/src/notifications/service.py declares
  `NotificationService.__init__(self, channel, retry_count)`; its only
  call sites, fixtures/src/billing/invoices.py and
  fixtures/src/billing/reminders.py, both outside the scope, pass
  `retry_count=3`.

  PASS if the reported findings include an `Unused configurability` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/src/notifications/service.py, that names `retry_count`, and
  whose ISSUE or SUGGESTION names at least one of the two call sites
  (invoices.py, reminders.py or fixtures/src/billing/) as passing the
  same value.
  FAIL if no finding reports `retry_count` as always receiving the same
  value, or if the finding is anchored (its FILE: line) on a file under
  fixtures/src/billing/.
weight: 2
---

Reports the parameter declared in scope that nothing varies, with the
outside call sites as evidence: the callers sit outside the scope and
must be read there, and the finding stays anchored on the declaration.

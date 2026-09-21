---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Async` (or clearly equivalent
  category name) finding on `complete_order` in
  fixtures/webhook_dispatcher.py, for calling
  `asyncio.create_task(notify_partner(...))` without keeping a reference to
  the task or handling its outcome, and without any comment/naming marking
  it as an intentional fire-and-forget call — so a failure inside
  `notify_partner` is silently lost.
  FAIL if no finding flags this unawaited/untracked task as a silent-failure
  risk.
weight: 1
---

Reports the untracked `asyncio.create_task(notify_partner(...))` in
`complete_order` as an `Async` finding.

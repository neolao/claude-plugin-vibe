---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Unused generality` (or clearly
  equivalent category name) finding on `send_notification`'s `channel`
  parameter in fixtures/discount.py, noting that all three call sites
  (`notify_order_placed`, `notify_order_shipped`, `notify_order_cancelled`)
  always pass `channel="email"`, so the `sms`/other branches are dead weight
  for this codebase.
  FAIL if no finding flags `channel` (or the unexercised `sms`/else branches)
  as unused generality.
weight: 1
---

Reports `send_notification`'s `channel` parameter as always receiving the
same value at every call site, an `Unused generality` finding.

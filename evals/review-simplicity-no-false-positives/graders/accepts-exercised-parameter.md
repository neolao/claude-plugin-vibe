---
type: llm
focus: last_message
criteria: |
  `send_notification`'s `channel` parameter in fixtures/clean_ops.py is
  called with three different values across its call sites: `"email"` from
  `notify_customer`, `"sms"` from `notify_support`, and a variable
  `endpoint` from `notify_webhook`.

  PASS if no `high` or `medium` severity finding calls `channel` unused
  generality or says its branches are dead.
  FAIL if it is flagged as Unused generality (or equivalent) at high or
  medium severity.
weight: 1
---

Does not call a genuinely varied parameter unused generality.

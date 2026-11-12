---
type: llm
focus: last_message
criteria: |
  fixtures/app/notify.py `after_refund` looks up `"order.refunded"` in
  `MESSAGES` (fixtures/i18n/messages.py), which defines only
  `order.confirmed`, `order.shipped` and `order.cancelled`: a refund
  notification raises KeyError.

  PASS if the reported findings include one anchored on
  fixtures/app/notify.py that names the `order.refunded` key and its
  absence from the catalogue (a KeyError or a missing message).
  FAIL if no finding names the `order.refunded` key.
weight: 2
---

Finds a key a template uses that the catalogue does not define.

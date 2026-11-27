---
type: llm
focus: last_message
criteria: |
  `notifier/payments.py` sets `STRIPE_KEY` to `os.environ.get("STRIPE_KEY",
  "sk_test_…")`: a test-mode Stripe key, committed as the default, that
  authenticates to the shop's test-mode account whenever the variable is
  unset.

  PASS if the reported findings include a `Secret` (or clearly equivalent
  category name) finding whose FILE: line points to notifier/payments.py,
  that names the committed `sk_test_` default, with `SEVERITY: medium`.
  FAIL if no finding reports the default key, if it is dismissed because
  the key is test-mode, or if it is rated `high` or `low`.
weight: 1
---

Reports a test-mode key of a real provider as a Secret at medium: it
still authenticates somewhere.

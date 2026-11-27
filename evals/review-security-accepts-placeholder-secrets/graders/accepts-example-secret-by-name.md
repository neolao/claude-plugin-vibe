---
type: llm
focus: last_message
criteria: |
  `EXAMPLE_WEBHOOK_SECRET` in notifier/webhooks.py is a well-formed
  `whsec_…` value that `setup_hint` prints to show what a signing secret
  looks like; `verify` uses `WEBHOOK_SECRET`, read from the environment.
  The name labels the value as an example.

  PASS if no `high` or `medium` severity `Secret` (or clearly equivalent
  category name) finding targets `EXAMPLE_WEBHOOK_SECRET`. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if `EXAMPLE_WEBHOOK_SECRET` is reported as a committed secret at
  high or medium severity.
weight: 1
---

Does not call a value its name labels as an example a committed secret.

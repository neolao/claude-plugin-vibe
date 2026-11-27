---
type: llm
focus: last_message
criteria: |
  `notifier/webhooks.py` commits `OLD_WEBHOOK_SECRET`, a well-formed
  `whsec_…` value, under a comment saying it was rotated after an
  incident. Nothing in the repository shows the rotation; the literal is
  still a committed signing secret.

  PASS if the reported findings include a `Secret` (or clearly equivalent
  category name) finding, at any severity, whose FILE: line points to
  notifier/webhooks.py and that names `OLD_WEBHOOK_SECRET` as a committed
  secret; a finding that says the rotation is the author's claim, or that
  the value should be removed regardless, passes.
  FAIL if no finding reports `OLD_WEBHOOK_SECRET`, or if it is dismissed
  because the comment says the value was rotated.
weight: 1
---

Reports a committed secret as it stands when a comment claims it was
rotated: the repository shows no rotation.

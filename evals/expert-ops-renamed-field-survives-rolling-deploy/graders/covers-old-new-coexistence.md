---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS says that, during the rollout,
  pods publishing the old message and pods publishing the new one run side by
  side, so the message must work for readers of either version: for example
  publishing both `carrier` and `carrier_code` for a transition period, or
  making readers accept either before any publisher switches.
  FAIL if the reply treats the change as a one-step switch (rename the field,
  deploy) with no mention that old and new publishers or readers overlap.
weight: 2
---

Requires the old and the new message shape to coexist during the rolling
rollout.

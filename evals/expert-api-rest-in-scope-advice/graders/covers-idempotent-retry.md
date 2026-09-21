---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  brief, that the Like endpoint must be safe to call twice (idempotent, or
  de-duplicated) because a flaky mobile client may automatically retry the
  same call after a timeout — and that a duplicate call must not register a
  second Like.
  FAIL if retry-safety/idempotency is missing entirely, or only stated as a
  generic "use idempotency keys" remark with no connection to the brief's
  retry-on-timeout scenario.
weight: 2
---

Names idempotency/retry-safety of the Like endpoint as a concrete requirement,
risk, or test scenario, tied to the brief's flaky-network retry detail.

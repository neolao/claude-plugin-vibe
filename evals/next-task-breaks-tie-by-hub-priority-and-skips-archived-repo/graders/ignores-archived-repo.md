---
type: llm
focus: last_message
criteria: |
  legacy-batch is listed in repos.md with status archived. Its item 001 has
  a waiting item in billing-api, but only `active` repos supply candidates.

  PASS if the presentation never offers a legacy-batch item as the pick or as
  a runner-up (it may mention it as the reason billing-api 002 is blocked).
  FAIL if a legacy-batch item is presented as a candidate, pick or runner-up.
weight: 2
---

Leaves the archived repo out of the candidates.

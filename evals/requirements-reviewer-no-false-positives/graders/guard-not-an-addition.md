---
type: llm
focus: last_message
criteria: |
  `filter_period` refuses a period whose start follows its end
  (fixtures/period.py:9-10). The agent's definition names exactly this case
  as not a finding: a guard on a parameter the request introduces serves the
  requirement.

  PASS if no `(addition)` finding targets the `start > end` guard, the
  `_in_period` helper, or the tests.
  FAIL if any of them is reported as an addition.
weight: 2
---

Input validation and private helpers are how, not what.

---
type: llm
focus: last_message
criteria: |
  `push_order` in fixtures/sync/client.py loops `range(MAX_RETRIES - 1)`
  while its docstring promises up to MAX_RETRIES retries after the first
  attempt (4 attempts in total for MAX_RETRIES = 3): the loop makes only
  2 attempts.

  PASS if the findings include one on `push_order` saying it makes fewer
  attempts than documented (a bounds or off-by-one issue), with SEVERITY
  `high` or `medium`.
  FAIL if no finding reports the attempt count, or it is rated `low`.
weight: 2
---

Reports the loop bound that gives fewer attempts than the contract states.

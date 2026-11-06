---
type: llm
focus: last_message
criteria: |
  `to_cents` in fixtures/billing/rounding.py truncates with `ROUND_DOWN`
  on a `Decimal` built from `str(amount)`, and `line_total_cents`
  truncates the unit price before multiplying. The accepted decision
  .vibe/decisions/001-amounts-are-truncated-to-the-cent.md mandates
  exactly that (never round, truncate per line).

  PASS if no `high` or `medium` severity finding claims `to_cents` or
  `line_total_cents` loses money, rounds the wrong way, or should round
  to nearest or truncate the total instead of the lines.
  FAIL if either is flagged as a wrong result at high or medium severity.
weight: 1
---

Does not reopen a behaviour an accepted decision mandates.

---
type: llm
focus: last_message
criteria: |
  `months_in` in fixtures/billing/periods.py returns
  `list(range(first, last))` and its docstring says "last excluded, like
  range"; `period_label` guards the empty case.

  PASS if no `high` or `medium` severity finding claims `months_in` drops
  its last month, is off by one, or that `period_label` fails on an empty
  range.
  FAIL if either is flagged as a Bounds issue (or equivalent) at high or
  medium severity.
weight: 1
---

Does not flag an exclusive range whose contract is exclusive: Python's
convention and the docstring agree.

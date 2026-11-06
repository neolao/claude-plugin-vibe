---
type: llm
focus: last_message
criteria: |
  fixtures/api/v1/contract.py lists `TICKET_FIELDS = ("reference",
  "status", "title")` and its docstring says v1 is frozen for the
  integrations still using it; fixtures/api/v2/contract.py lists the
  current five fields.

  PASS if no `high` or `medium` severity finding names the two
  `TICKET_FIELDS` tuples, fixtures/api/v1/contract.py or
  fixtures/api/v2/contract.py as a duplicated case list, a parallel table
  or any coordination to maintain. A `low` finding passes, and so does a
  report with no findings at all.
  FAIL if the v1/v2 field lists are flagged at high or medium severity.
weight: 1
---

Does not report a frozen contract kept beside the current one: a copy
meant to stand still while the other moves is not coordination.

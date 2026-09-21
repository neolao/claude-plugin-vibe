---
type: llm
focus: last_message
criteria: |
  `Money` in fixtures/money.py is a `@dataclass(frozen=True)` compared by
  value, and `add` returns a new instance after checking currency.

  PASS if no `high` or `medium` severity Value object finding claims it is
  mutable or compared by identity.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a frozen, value-compared Money mutable.

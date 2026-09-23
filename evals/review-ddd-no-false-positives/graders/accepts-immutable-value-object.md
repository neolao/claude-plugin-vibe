---
type: llm
focus: last_message
criteria: |
  `Money` in fixtures/money.py is a `@dataclass(frozen=True)` compared by
  value; `add` and `times` return new instances, and `add`/`exceeds` check
  the currency. `OrderApprovalService` computes the order total and the
  threshold comparison through `Money`, not on raw numbers.

  PASS if no `high` or `medium` severity Value object finding claims it is
  mutable, compared by identity, or bypassed by raw-number arithmetic.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a frozen, value-compared Money mutable.

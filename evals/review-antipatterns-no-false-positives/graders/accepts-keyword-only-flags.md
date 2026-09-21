---
type: llm
focus: last_message
criteria: |
  `PaymentGateway.charge` declares `retry` and `notify` keyword-only, and
  every call site passes them by name (`charge(order, retry=True,
  notify=False)`), so each flag's meaning is visible where it is used.

  PASS if no `high` or `medium` severity Boolean blindness finding targets
  these calls.
  FAIL if they are flagged at high or medium severity.
weight: 1
---

Does not call named keyword flags boolean blindness.

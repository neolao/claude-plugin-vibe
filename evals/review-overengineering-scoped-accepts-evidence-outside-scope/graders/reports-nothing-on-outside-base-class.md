---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/src/notifications/.
  fixtures/src/billing/pricing.py, outside the scope, declares a
  `PricingStrategy` base class that `StandardPricing` alone implements;
  no file in scope uses either.

  PASS if no finding reports `PricingStrategy` or `StandardPricing` —
  whatever its severity and wherever its FILE: line points. A report
  with no findings at all passes, and so does a sentence outside any
  finding block saying the base class exists but is out of scope.
  FAIL if any finding (a FILE: block) reports `PricingStrategy` or
  `StandardPricing`.
weight: 2
---

Reports nothing on a one-implementation base class declared and used
outside the scope, however visible: the full review owns it.

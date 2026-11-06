---
type: llm
focus: last_message
criteria: |
  `PricingPolicy` in fixtures/services/pricing.py is a `Protocol`
  implemented by `StandardPricing` and `WholesalePricing` in the same
  file and chosen by `policy_for`: an interface between types of one
  layer, implemented by no adapter and reaching no external system.

  PASS if no finding of any severity targets `PricingPolicy`,
  `StandardPricing`, `WholesalePricing` or `policy_for` as a port, a
  leaky port, a misplaced port or a wiring defect. A report with no
  findings at all passes.
  FAIL if any of them is reported as a port or wiring finding.
weight: 1
---

Does not call an interface between two classes of the same layer a port.

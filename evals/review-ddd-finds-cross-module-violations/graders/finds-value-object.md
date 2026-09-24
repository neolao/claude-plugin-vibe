---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Value object` (or clearly
  equivalent category name) finding on `Address` (fixtures/shop/address.py,
  a non-frozen dataclass compared by value) for being mutable, or on
  `update_street` in fixtures/shop/customer_service.py for editing
  `customer.address.street` in place instead of replacing the address.
  Either anchor is enough. Mentioning that household members share one
  `Address` instance (fixtures/shop/household.py) is welcome but not
  required.
  FAIL if no finding flags `Address`'s mutability or its in-place edit.
weight: 1
---

Reports the mutable `Address` value object, or its in-place edit from the
customer service, as a Value object finding.

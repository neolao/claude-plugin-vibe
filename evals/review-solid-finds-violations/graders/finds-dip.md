---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `D` (or clearly equivalent DIP)
  finding on `OrderProcessor.__init__`, for constructing a concrete
  `StripeClient` directly with no seam (interface or injected dependency) to
  substitute it.
  FAIL if no finding flags this concrete construction as a DIP violation.
weight: 1
---

Reports `OrderProcessor` constructing `StripeClient` directly as a `D`
finding.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `God object` / `God function` (or
  clearly equivalent category name) finding on `OrderWorkflow` in
  fixtures/order_workflow.py, for owning every step of the order lifecycle
  (validate, price, charge, ship, email) on one class instead of splitting
  the responsibilities.
  FAIL if no finding flags `OrderWorkflow` for this reason.
weight: 1
---

Reports `OrderWorkflow`'s do-everything lifecycle as a God object/function
finding.

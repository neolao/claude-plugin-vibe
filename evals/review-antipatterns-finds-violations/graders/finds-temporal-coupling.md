---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Temporal coupling` (or clearly
  equivalent category name) finding on `OrderWorkflow` in
  fixtures/order_workflow.py, for requiring `init()` to be called before
  `run()` with nothing in the API enforcing that order.
  FAIL if no finding flags this required call order.
weight: 1
---

Reports `OrderWorkflow.init`/`run`'s required call order as a Temporal
coupling finding.

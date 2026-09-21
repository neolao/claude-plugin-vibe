---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Boolean blindness` (or clearly
  equivalent category name) finding on the `self._charge(order, True, False)`
  call in `OrderWorkflow.run` (fixtures/order_workflow.py), for positional
  booleans whose meaning is invisible at the call site.
  FAIL if no finding flags this call site's unclear booleans.
weight: 1
---

Reports the `self._charge(order, True, False)` call site as a Boolean
blindness finding.

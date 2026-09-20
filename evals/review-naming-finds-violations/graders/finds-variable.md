---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Variable` (or clearly equivalent
  category name) finding on `OrderProcessor.calc` in fixtures/order_processor.py,
  for the cryptic parameter/variable names `o` and `t` that need decoding to
  understand they mean "order" and "total".
  FAIL if no finding flags these names as unclear.
weight: 1
---

Reports the cryptic `o`/`t` names in `OrderProcessor.calc` as a `Variable`
finding.

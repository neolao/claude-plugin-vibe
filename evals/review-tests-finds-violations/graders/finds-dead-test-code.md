---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dead test code` (or clearly
  equivalent category name) finding on `test_divide_by_zero` in
  fixtures/test_calculator.py, for being decorated with `@unittest.skip`
  with no reason string explaining why it is skipped.
  FAIL if no finding flags the unexplained `@unittest.skip`.
weight: 1
---

Reports the unexplained `@unittest.skip` on `test_divide_by_zero` as a
`Dead test code` finding.

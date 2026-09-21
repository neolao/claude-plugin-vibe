---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dead test code` (or clearly
  equivalent category name) finding on `test_divide_by_zero` in
  fixtures/test_calculator.py, for being decorated with `@unittest.skip`
  with no reason string explaining why, checked against the real skip
  count from the suite run.
  FAIL if no finding flags the unexplained `@unittest.skip`.
weight: 1
---

Reports `test_divide_by_zero`'s unexplained `@unittest.skip` as a `Dead
test code` finding.

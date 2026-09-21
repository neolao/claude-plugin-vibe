---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Missing negative cases` (or
  clearly equivalent category name) finding noting that `divide`'s
  divide-by-zero error path in fixtures/calculator.py has no *active* test
  covering it — `test_divide_by_zero` in fixtures/test_calculator.py exists
  but is skipped, so the negative case is currently unverified.
  FAIL if no finding flags the divide-by-zero path as lacking active
  negative-case coverage.
weight: 1
---

Reports the unverified divide-by-zero error path as a `Missing negative
cases` finding.

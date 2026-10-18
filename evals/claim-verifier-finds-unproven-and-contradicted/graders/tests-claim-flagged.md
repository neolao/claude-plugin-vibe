---
type: llm
focus: last_message
criteria: |
  "All 5 tests pass": no test command or output was provided, and
  fixtures/test_parser.py holds 2 tests, not 5.

  PASS if a finding quotes that claim and flags it as `(unproven)` (no
  output provided) or `(contradicted)` (the file holds 2 tests, or a re-run
  shows 2), with a fix (run the tests and quote the output, or correct the
  count).
  FAIL if the claim is accepted, or if the finding neither mentions the
  missing output nor the real number of tests.
weight: 2
---

"Tests pass" without the command and its output is not a fact.

---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/README.md alone. The rest of fixtures/ holds an
  assertion-free test (fixtures/tests/test_rates.py, `assertTrue(True)`)
  and two untested error branches (fixtures/billing/invoice.py,
  fixtures/shipping/rates.py), all outside the scope.

  PASS if the report contains no finding at all (no `FILE:` block on any
  file). A sentence outside any finding block saying nothing in scope is
  code or a test, or that the rest of the repository was not reviewed,
  passes.
  FAIL if any finding (a `FILE:` block) is reported, whatever its file or
  category — on test_rates.py, invoice.py, rates.py or README.md.
weight: 2
---

Reports nothing on a scope with no code and no test, and never reviews
the rest of the codebase instead, however poor its tests.

---
type: llm
focus: last_message
criteria: |
  `test_net_pay_applies_tax_rate` in fixtures/test_payroll.py patches
  `payroll.net_pay` itself with `return_value=800.0` and asserts that
  `payroll.net_pay(1000, 0.2)` returns 800.0: no line of `net_pay` runs,
  and CLAUDE.md names `net_pay` as the critical logic of the service. A
  wrong `net_pay` ships green.

  PASS if an `Over-mocked` (or clearly equivalent category name, such as
  `Tautological`) finding on this test, for patching the function under
  test, carries `SEVERITY: high`.
  FAIL if no finding reports the test for stubbing `net_pay` itself, or
  if that finding is rated medium or low.
weight: 2
---

A stub of the code under test lets a regression ship green: high, never
lower.

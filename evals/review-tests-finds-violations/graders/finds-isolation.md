---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Isolation` (or clearly
  equivalent category name) finding on the module-level `_shared_state`
  dict in fixtures/test_user_service.py, mutated by
  `test_deactivate_user_marks_inactive` and asserted against in the same
  test — a pattern whose correctness depends on how many times the module
  has run in this process / test execution order, instead of using a fresh
  per-test fixture.
  FAIL if no finding flags `_shared_state` as order-dependent shared state
  between tests.
weight: 1
---

Reports the module-level `_shared_state` mutation as an `Isolation`
finding.

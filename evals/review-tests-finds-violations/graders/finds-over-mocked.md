---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Over-mocked` (or clearly
  equivalent category name, such as `Tautological` when the finding says the
  test only observes a mock's configured value) finding on
  `test_get_user_returns_active_flag` in fixtures/test_user_service.py, for
  patching `UserService.get_user` itself — the very method under test — so
  the assertion only reads back the `return_value` the test configured and
  no line of `get_user` runs.
  FAIL if no finding flags this test for mocking the code under test.
weight: 1
---

Reports `test_get_user_returns_active_flag` patching the method it claims to
test as an `Over-mocked` finding.

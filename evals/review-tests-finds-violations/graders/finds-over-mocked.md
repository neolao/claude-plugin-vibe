---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Over-mocked` (or clearly
  equivalent category name) finding on `test_get_user` in
  fixtures/test_user_service.py, for configuring `self.db.get.return_value`
  and then only checking that the mock's own configured value came back,
  which verifies nothing about `UserService.get_user` itself.
  FAIL if no finding flags `test_get_user` as over-mocked / only asserting
  the mock's own return value.
weight: 1
---

Reports `test_get_user` asserting only the mock's own configured return
value as an `Over-mocked` finding.

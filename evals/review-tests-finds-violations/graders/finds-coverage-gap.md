---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Coverage gap` (or clearly
  equivalent category name) finding on `UserService.deactivate_user` in
  fixtures/user_service.py, for its `ValueError` branch (raised when the
  user is not found) having no test at all in
  fixtures/test_user_service.py.
  FAIL if no finding flags the untested `deactivate_user` error branch.
weight: 1
---

Reports `deactivate_user`'s untested "user not found" branch as a
`Coverage gap` finding.

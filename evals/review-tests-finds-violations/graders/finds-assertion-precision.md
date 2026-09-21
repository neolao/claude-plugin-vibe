---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Assertion precision` (or
  clearly equivalent category name) finding on `test_get_user` in
  fixtures/test_user_service.py, for using `assertIsNotNone(result)` where
  a precise `assertEqual` against the expected user dict would actually
  verify the returned value.
  FAIL if no finding flags the broad `assertIsNotNone` matcher.
weight: 1
---

Reports `test_get_user`'s broad `assertIsNotNone` matcher as an `Assertion
precision` finding.

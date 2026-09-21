---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Implementation-coupled` (or
  clearly equivalent category name) finding on `test_memoizer_caches_internally`
  in fixtures/test_calculator.py, for asserting on the private `_cache`
  attribute of `Memoizer` directly instead of going through the public
  `compute()` behaviour, which would break on any pure refactor of the
  caching strategy.
  FAIL if no finding flags this test's reliance on the private `_cache`
  attribute.
weight: 1
---

Reports `test_memoizer_caches_internally` reaching into the private
`_cache` dict as an `Implementation-coupled` finding.

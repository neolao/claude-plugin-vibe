---
type: llm
focus: last_message
criteria: |
  fixtures/shipping/rates.py is outside the scope, although its test file
  fixtures/tests/test_rates.py is in it. Its `raise KeyError` on an
  unknown zone has no test.

  PASS if no finding (a `FILE:` block) is anchored on
  fixtures/shipping/rates.py, and no finding reports the unknown-zone
  branch as untested — whatever its FILE: line. A sentence outside any
  finding block saying that `rate_for`'s error branch is untested but out
  of scope passes, and so does a SUGGESTION on the test_rates.py finding
  that mentions asserting the error.
  FAIL if any finding is anchored on fixtures/shipping/rates.py, or if a
  `Coverage gap` / `Missing negative cases` finding reports the
  unknown-zone branch.
weight: 1
---

A coverage gap goes on the source file, and only when that file is in
scope: a test file in scope does not pull its module's gaps in with it.

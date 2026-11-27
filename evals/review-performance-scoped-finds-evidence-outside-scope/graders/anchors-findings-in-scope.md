---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/shipping/. Files outside it
  (fixtures/api/app.py, fixtures/api/reports.py) may be named inside a
  finding's ISSUE or SUGGESTION as the caller that makes a path hot or the
  feeder that makes a map grow. fixtures/api/reports.py holds
  `monthly_volume`, which loops over the active customers and runs one
  `count(*)` query per customer: both the loop and the query sit outside
  the scope, and no file under fixtures/shipping/ takes part in it.

  PASS if every finding's FILE: line points to a file under
  fixtures/shipping/, and no finding reports `monthly_volume` or its
  per-customer `count(*)` query — whatever its FILE: line. A sentence
  outside any finding block saying that `monthly_volume` has an N+1 but is
  out of scope passes.
  FAIL if any finding is anchored (its FILE: line) on a file outside
  fixtures/shipping/, or if any finding (a FILE: block) reports
  `monthly_volume` or its per-customer query.
weight: 2
---

Keeps every finding anchored on a file in scope and leaves a defect whose
both ends sit outside the scope alone, however clear: the whole repository
is read for evidence, and the full review owns the rest.

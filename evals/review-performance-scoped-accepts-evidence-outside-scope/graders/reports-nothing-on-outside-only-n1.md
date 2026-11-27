---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was fixtures/shipping/.
  fixtures/api/reports.py, outside the scope, holds `monthly_volume`,
  which loops over the active customers and runs one `count(*)` query per
  customer: both the loop and the query sit outside the scope, and no file
  under fixtures/shipping/ takes part in it.

  PASS if no finding reports `monthly_volume` or its per-customer
  `count(*)` query — whatever its severity and wherever its FILE: line
  points. A report with no findings at all passes, and so does a sentence
  outside any finding block saying the N+1 exists but is out of scope.
  FAIL if any finding (a FILE: block) reports `monthly_volume` or its
  per-customer query.
weight: 2
---

Reports nothing on an N+1 whose loop and query both sit outside the
scope, however clear: the full review owns it.

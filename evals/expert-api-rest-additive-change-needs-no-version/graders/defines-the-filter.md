---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or TEST SCENARIOS defines the behaviour of the new
  `?status=` filter in at least one concrete respect: the response to an
  unknown status value (an error with a precise status code, not an empty
  list or a silent ignore), or the list returning the same results as today
  when the filter is absent.
  FAIL if the filter's behaviour is never defined beyond "add a status
  filter", or if an unknown status value is said to return the unfiltered
  list.
weight: 1
---

Defines the new filter — the unknown-value case or the absent-filter case
— instead of spending the lists on versioning that is not needed.

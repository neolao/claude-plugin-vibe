---
type: llm
focus: last_message
criteria: |
  `pay_slip_label` in fixtures/labels.py raises `ValueError` on a blank
  employee name; fixtures/test_labels.py covers the join and the strip,
  not that branch. CLAUDE.md names `net_pay` as the critical logic, not
  the label helper.

  PASS if a `Coverage gap` (or clearly equivalent category name, such as
  `Missing negative cases`) finding reports the untested blank-name
  branch of `pay_slip_label` and carries `SEVERITY: medium`.
  FAIL if no finding reports that branch, or if the finding is rated
  high or low.
weight: 1
---

An untested branch of a non-critical helper is a case unverified here:
medium, not high.

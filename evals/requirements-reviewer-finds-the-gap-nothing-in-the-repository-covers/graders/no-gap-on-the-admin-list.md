---
type: llm
focus: last_message
criteria: |
  Criterion 2 (the admin coupon list shows each coupon's expiry date) is
  met by `coupon_rows` in fixtures/admin.py, a file the change did not
  touch and that is not among the files handed over as the deliverable.
  The agent's definition says a criterion already met by code the change
  did not need to touch is met.

  PASS if no `(gap)` finding targets criterion 2 or the admin list. A
  sentence inside another finding, or a bullet of another type, that
  mentions admin.py as outside the changed files does not count as a gap.
  FAIL if a `(gap)` finding reports the admin list or the expiry date as
  uncovered.
weight: 2
---

A criterion met by untouched code is met; only what nothing in the
repository covers is a gap.

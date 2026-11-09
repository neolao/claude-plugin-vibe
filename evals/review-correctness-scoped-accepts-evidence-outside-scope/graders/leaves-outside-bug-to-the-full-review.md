---
type: llm
focus: last_message
criteria: |
  `months_in` in fixtures/reports/periods.py returns `list(range(first,
  last))` under a docstring that promises both ends included, and
  `quarter_label` in fixtures/reports/summary.py relies on it: a real
  off-by-one, but both the helper and its caller lie outside the scope
  (fixtures/orders/), and nothing in fixtures/orders/ calls `months_in`.

  PASS if no finding is anchored (its FILE: line) on a file outside
  fixtures/orders/ and no finding reports the `months_in` off-by-one or
  `quarter_label`, whatever its anchor.
  FAIL if any finding's FILE: line points outside fixtures/orders/, or if
  any finding reports `months_in` or `quarter_label`.

  Only the FILE: line anchors a finding: an outside file merely named in
  a finding's ISSUE or SUGGESTION (as evidence, or as another place the
  same fix would apply) is not a finding anchored there, unless it
  reports the `months_in` off-by-one or `quarter_label`.

  A sentence outside any finding block that says the `months_in`
  off-by-one exists but was left out of the report (for the full review)
  is the expected behavior, not a finding: PASS.
weight: 1
---

Leaves a bug whose both ends lie outside the scope to the full review:
the scope bounds what is reported, and no in-scope file takes part in
this one.

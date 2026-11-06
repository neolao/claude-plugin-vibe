---
type: llm
focus: last_message
criteria: |
  fixtures/pricing/amounts.py carries `# TODO(#231): JPY has no minor unit,
  the *100 is wrong for it` (a ticketed marker) and
  fixtures/bin/import_prices.py carries `# TODO: skip the rows the supplier
  marks as discontinued` (a bare marker). Both are review-hygiene's Stale
  marker axis, not review-comments'.

  PASS if no finding, at any severity, targets either TODO. A report with
  no findings at all passes, and so does a report that mentions a TODO only
  to say it is review-hygiene's.
  FAIL if either TODO is flagged as redundant, verbose, misleading, stale
  or anything else.
weight: 1
---

Leaves TODO markers to review-hygiene, tracked or not: a bare TODO is that
agent's Stale marker and must not be reported twice.

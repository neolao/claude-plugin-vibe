---
type: llm
focus: last_message
criteria: |
  The request's constraint: "Do not change the signature of
  `export_report(rows, month)`". The deliverable's signature is
  `export_report(rows, month, fmt="csv")` (fixtures/export.py:21).

  PASS if a `(constraint)` finding quotes that constraint and points at the
  added `fmt` parameter at line 21, with a fix.
  FAIL if the signature change is not reported as a constraint breach (a
  mention of it only inside the JSON addition finding does not count: the
  constraint is its own requirement).
weight: 2
---

An explicit constraint of the request, breached, is its own finding.

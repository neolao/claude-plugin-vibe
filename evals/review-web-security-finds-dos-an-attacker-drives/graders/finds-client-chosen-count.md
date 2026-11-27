---
type: llm
focus: last_message
criteria: |
  `export` in fixtures/app.py reads `rows` from the query string and
  passes it to `render_export`, which builds that many lines, with no
  upper bound: one request names any count.

  PASS if the reported findings include a `DoS` (or clearly equivalent
  category name) finding on `export` or its `rows` parameter, for the
  missing upper bound.
  FAIL if no finding reports the uncapped `rows`.
weight: 2
---

Reports a client-chosen count passed on with no upper bound as DoS.

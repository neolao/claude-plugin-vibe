---
type: llm
focus: last_message
criteria: |
  The request asks for a total line and nothing about labels. The first
  hunk of fixtures/change.diff rewrites `format_label` (a loop replaced by
  a generator expression, the parameter renamed `text`) with the same
  behaviour: a change to code no requirement needed touched. In the
  resulting file it is fixtures/export.py lines 7-8.

  PASS if an `(addition)` finding points at the `format_label` rewrite (the
  hunk in change.diff and/or export.py lines 7-8) and says no requirement
  covers it, with a fix (leave the function as it was, or drop the hunk).
  FAIL if the rewrite of `format_label` is not reported as an addition.
weight: 2
---

A refactor of code the request did not need touched is an addition, even
though nothing visible changes.

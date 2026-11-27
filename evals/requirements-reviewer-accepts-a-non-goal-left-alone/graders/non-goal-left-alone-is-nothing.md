---
type: llm
focus: last_message
criteria: |
  The request puts the gallery thumbnails out of scope. fixtures/
  thumbnails.py is not among the changed files and still reads
  `THUMB_WIDTH = 120`: the non-goal is respected. No dependency is added
  (standard library only).

  PASS if no finding of any type (`gap`, `addition`, `constraint`,
  `ambiguity`) mentions the thumbnails, their width, or a dependency.
  FAIL if the thumbnails are reported as a gap (something to deliver), as
  a constraint, or as an ambiguity, or if a dependency finding appears.
weight: 2
---

A non-goal left alone is nothing to report.

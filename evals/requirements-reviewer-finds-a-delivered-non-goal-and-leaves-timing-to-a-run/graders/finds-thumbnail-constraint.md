---
type: llm
focus: last_message
criteria: |
  The request's first constraint puts the gallery thumbnails out of
  scope: "keep their current width (120 px); this change does not touch
  them". fixtures/thumbnails.py is among the changed files and sets
  `THUMB_WIDTH = 160` (line 3).

  PASS if a `(constraint)` finding quotes that out-of-scope sentence and
  points at `THUMB_WIDTH = 160` in thumbnails.py, with a fix (restore 120,
  leave the file out of the change).
  FAIL if the thumbnail change is not reported, or is reported only as an
  `(addition)`: a non-goal the request states is a constraint, and the
  finding quotes it.
weight: 2
---

A non-goal delivered anyway breaches the sentence that excluded it.

---
type: llm
focus: last_message
criteria: |
  `export` in fixtures/app.py parses `rows` as an integer and clamps it
  between 1 and `MAX_EXPORT_ROWS` before building the export, whatever
  the client sends.

  PASS if no `high` or `medium` severity `DoS` (or clearly equivalent
  category name) finding targets `export` or its `rows` parameter. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if the clamped count is reported as unbounded at high or medium
  severity.
weight: 2
---

Does not call a clamped count a DoS.

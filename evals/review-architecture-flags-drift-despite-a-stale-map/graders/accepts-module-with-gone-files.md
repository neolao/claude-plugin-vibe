---
type: llm
focus: last_message
criteria: |
  `.vibe/modules/reports.md` lists `reports/weekly.py`, a file that no
  longer exists in fixtures/ — no `reports/` directory at all. Nothing can
  import a file that is gone.

  PASS if no `high` or `medium` severity Orphaned module (or Module scope)
  finding targets the `reports` module. A report with no findings at all
  passes.
  FAIL if `reports` is reported as orphaned, or as drift, at high or
  medium severity.
weight: 1
---

Does not call a module whose listed files are gone an orphan: that is a
stale map.

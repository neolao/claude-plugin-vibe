---
type: llm
focus: last_message
criteria: |
  `Report.render()` in fixtures/receipts/report.py raises `RuntimeError`
  when `load()` was not called first; the only caller,
  fixtures/receipts/end_of_day.py, calls them in order.

  PASS if no `high` or `medium` severity Temporal coupling (or
  equivalent) finding targets `Report`, `load` or `render`. A `low`
  finding passes, as does a report with no findings at all.
  FAIL if the order is flagged at high or medium severity.
weight: 1
---

A required order that fails loudly when broken is a contained match: `low`
at most.

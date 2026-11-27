---
type: llm
focus: last_message
criteria: |
  `render_report(report, fmt="plain")` in fixtures/report_renderer.py
  branches on `fmt` in its own body (`if fmt == "html"`); its three
  callers (fixtures/daily_report.py, fixtures/weekly_report.py,
  fixtures/report_archive.py) all pass `fmt="plain"`. That is a plain
  function parameter the function branches on, which belongs to
  review-simplicity's unused generality, not to this agent.

  PASS if no finding (a FILE: block) names `fmt`, `render_report` or its
  unexercised `html` branch — whatever its category and severity. A
  report with no findings at all passes, and so does a sentence outside
  any finding block saying the parameter is review-simplicity's.
  FAIL if any finding (a FILE: block) reports `fmt`, `render_report` or
  the `html` branch, under Unused configurability or any other category.
weight: 2
---

Leaves a function parameter the body branches on to review-simplicity:
the same parameter reported by two agents is merged on every run.

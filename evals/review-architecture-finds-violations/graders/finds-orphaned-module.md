---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Orphaned module` (or clearly
  equivalent category name) finding on `fixtures/utils/legacy_report.py`,
  for a module nothing else in the codebase imports or depends on, and
  which is not an entry point — while `.vibe/modules/csv-export.md` claims
  it depends on `core`.
  FAIL if no finding flags `legacy_report.py` as orphaned.
weight: 1
---

Reports `legacy_report.py` — imported by nothing, reached by nothing — as an
`Orphaned module` finding.

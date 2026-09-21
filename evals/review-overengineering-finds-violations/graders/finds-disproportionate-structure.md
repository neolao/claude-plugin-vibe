---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Disproportionate structure` (or
  clearly equivalent category name) finding on the
  `ReportController` -> `ReportFormatterService` -> `ReportRepository` chain
  in fixtures/report_cache.py, for splitting a dict lookup and one f-string
  format across three classes/layers where a single function would do.
  FAIL if no finding flags this three-class chain as out of proportion to
  the work it does.
weight: 1
---

Reports the controller/service/repository split in fixtures/report_cache.py
as a `Disproportionate structure` finding.

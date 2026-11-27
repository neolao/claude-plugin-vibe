---
type: llm
focus: last_message
criteria: |
  `ReportController.handle` in fixtures/src/reports/controller.py calls
  `ReportService.title` in fixtures/src/reports/service.py, which calls
  `ReportRepository.fetch` in fixtures/src/reports/repository.py: three
  classes in three files around one dict lookup and one key read.

  PASS if the reported findings include a `Disproportionate structure`
  (or clearly equivalent category name) finding on this chain (anchored
  on any of the three files, naming the controller/service/repository
  split) with SEVERITY `medium`.
  FAIL if no finding reports the three-class chain as out of proportion,
  or if that finding carries SEVERITY `high` or `low`.
weight: 2
---

Reports the three-layer chain at `medium`: a reader crosses three files
to follow one lookup, a cost paid today.

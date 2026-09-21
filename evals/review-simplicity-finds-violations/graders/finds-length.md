---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Length` (or clearly equivalent
  category name) finding on `generate_report` in
  fixtures/report_generator.py, for being a long function (over 40 lines)
  built from many sequential string-append statements.
  FAIL if no finding flags `generate_report`'s length.
weight: 1
---

Reports `generate_report`'s length (over 40 lines) as a `Length` finding.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Complexity` (or clearly
  equivalent category name) finding on `classify_order` in
  fixtures/report_generator.py, for cyclomatic complexity clearly above the
  10-branch threshold (the function has around a dozen or more decision
  points across its status/total branches).
  FAIL if no finding flags `classify_order` as a complexity hotspot.
weight: 1
---

Reports `classify_order`'s branching as a `Complexity` finding.

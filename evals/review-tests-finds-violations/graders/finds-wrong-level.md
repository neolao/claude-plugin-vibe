---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Wrong level` (or clearly
  equivalent category name) finding on `test_add_writes_result_to_disk` in
  fixtures/test_calculator.py, for doing a real `time.sleep` and real
  filesystem I/O inside what this suite treats as a fast unit test —
  behaving like an integration-level test hiding among unit tests.
  FAIL if no finding flags this test's real sleep/disk I/O as being at the
  wrong test level.
weight: 1
---

Reports `test_add_writes_result_to_disk`'s real sleep and disk I/O as a
`Wrong level` finding.

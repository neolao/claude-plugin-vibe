---
type: llm
focus: last_message
criteria: |
  `.vibe/modules/metrics.md` lists fixtures/metrics/collector.py, which is
  in scope. No file imports `metrics` (grep finds no importer), it is not
  an entry point, and no manifest or framework loads it.

  PASS if the reported findings include an `Orphaned module` (or clearly
  equivalent category name) finding on the `metrics` module or on
  fixtures/metrics/collector.py.
  FAIL if no finding flags `metrics` as orphaned.
weight: 2
---

Reports the module added in scope that nothing wires in.

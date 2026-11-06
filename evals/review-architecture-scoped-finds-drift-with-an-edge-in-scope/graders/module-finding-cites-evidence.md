---
type: llm
focus: last_message
criteria: |
  A `MODULE:` finding names a module file (`metrics.md`), which the
  classifier cannot re-read as code: the agent's definition says such a
  finding still cites the `path:line` evidence in its ISSUE.

  PASS if the finding on the `metrics` module (whether its first line is
  `MODULE:` or `FILE:`) names the path fixtures/metrics/collector.py
  (or `metrics/collector.py`) somewhere in its lines, with or without a
  line number.
  FAIL if the `metrics` finding names only the module (`metrics`,
  `metrics.md`) and no file path, or if there is no finding on `metrics`
  at all.
weight: 1
---

Cites the file behind a module-level finding, so the classifier can re-read
it.

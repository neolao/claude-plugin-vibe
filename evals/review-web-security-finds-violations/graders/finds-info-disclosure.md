---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Info disclosure` (or clearly
  equivalent category name) finding on `whoami` in fixtures/app.py, for
  returning the raw exception message (`str(e)`, which leaks an internal
  file path) directly to the client.
  FAIL if no finding flags `whoami`'s raw exception message being returned
  to the client.
weight: 1
---

Reports `whoami`'s raw exception message returned to the client as an
`Info disclosure` finding.

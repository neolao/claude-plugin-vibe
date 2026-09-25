---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Unused` finding on `click`
  in fixtures/pyproject.toml, noting that it is never imported anywhere in
  fixtures/src/ or fixtures/tests/.
  FAIL if `click` is not flagged as unused.
weight: 1
---

Reports the declared-but-never-imported `click` as an Unused finding.

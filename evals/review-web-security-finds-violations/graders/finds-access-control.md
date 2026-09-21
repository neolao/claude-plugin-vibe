---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name) finding, rated high severity, on `delete_user`
  in fixtures/app.py, for having no authentication or authorization check
  before performing a destructive admin action.
  FAIL if no finding flags `delete_user`'s missing auth check, or if it is
  rated low/medium instead of high.
weight: 2
---

Reports `delete_user`'s missing authentication/authorization check as a
high-severity `Access control` finding.

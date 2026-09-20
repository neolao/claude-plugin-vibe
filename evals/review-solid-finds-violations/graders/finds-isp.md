---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `I` (or clearly equivalent ISP)
  finding on `ReportGenerator.generate`, for taking the whole 8-field `User`
  object but only reading `name` and `email` from it.
  FAIL if no finding flags `ReportGenerator.generate` for this reason.
weight: 1
---

Reports `ReportGenerator.generate` reading only two fields off a large `user`
object as an `I` finding.

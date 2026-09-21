---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Duplication` (or clearly
  equivalent category name) finding pointing at `validate_email_signup` and
  `validate_email_login` in fixtures/validators.py being an identical,
  copy-pasted block of validation checks.
  FAIL if no finding flags these two functions as duplicated.
weight: 1
---

Reports `validate_email_signup` and `validate_email_login` in
fixtures/validators.py as a `Duplication` finding.

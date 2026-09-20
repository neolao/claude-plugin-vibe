---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Secret` (or clearly equivalent category name)
  finding pointing at the hardcoded `AWS_SECRET_KEY` value in fixtures/app.py, rated
  high or medium severity.
  FAIL if no finding mentions the hardcoded credential, or if it is dismissed as fine.
weight: 1
---

Reports the hardcoded AWS secret key as a Secret finding.

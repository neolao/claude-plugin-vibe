---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Injection` finding on the SQL query
  in `get_user`, built by concatenating the `username` argument into the
  statement string.
  FAIL if that query is not flagged as an injection risk.
weight: 1
---

Reports the concatenated SQL query in `get_user` as an Injection finding.

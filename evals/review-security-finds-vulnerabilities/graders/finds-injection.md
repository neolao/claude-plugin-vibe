---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include at least one `Injection` finding covering either:
  - the SQL query built by string concatenation with `username` in `get_user`, or
  - the `subprocess.run(..., shell=True)` call built by string concatenation with
    `filename` in `run_backup`.
  Either one alone is enough to pass; both is fine too.
  FAIL if neither concatenation-built command/query is flagged as an injection risk.
weight: 2
---

Reports at least one of the two injection points (SQL concatenation or shell=True
concatenation) as an Injection finding.

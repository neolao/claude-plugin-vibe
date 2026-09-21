---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Injection` finding on
  `subprocess.run(..., shell=True)` in `run_backup`, whose command string is
  built by concatenating the `filename` argument.
  FAIL if that call is not flagged as an injection risk.
weight: 1
---

Reports the concatenated `shell=True` command in `run_backup` as an Injection
finding.

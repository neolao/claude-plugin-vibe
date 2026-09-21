---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  specific brief, that `prune-logs` must return distinct, documented non-zero
  exit codes per failure class (e.g. directory not found, permission denied,
  partial deletion failure) so unattended cron jobs can detect and alert on
  failure, and never exit 0 after a failure.
  FAIL if the reply never raises exit-code correctness for the cron/unattended
  use case, or only mentions exit codes in the abstract without tying them to
  cron failure detection.
weight: 2
---

Names exit-code correctness tailored to unattended cron-job failure
detection.

---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  specific brief, that the deleted-file-path list piped into other tools must
  go to stdout while progress/diagnostic messages (and cron-job noise) go to
  stderr, so the piped output stays clean and machine-parseable — not a
  generic "use stdout/stderr correctly" restatement.
  FAIL if the reply never distinguishes stdout data from stderr diagnostics
  for this command's piping use case.
weight: 2
---

Names the stdout-for-data / stderr-for-diagnostics split needed for the
piped deleted-file-list use case.

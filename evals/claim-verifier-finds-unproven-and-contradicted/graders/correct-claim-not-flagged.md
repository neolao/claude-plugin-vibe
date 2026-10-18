---
type: llm
focus: last_message
criteria: |
  "`read_contacts` reads the file line by line and splits each line on
  commas (fixtures/parser.py:7-11)" is correct: `splitlines()` then
  `line.split(",")`.

  PASS if no finding targets that claim.
  FAIL if it is reported as unproven, contradicted, or an over-reaching
  conclusion.
weight: 1
---

A correct, sourced claim is not a finding.

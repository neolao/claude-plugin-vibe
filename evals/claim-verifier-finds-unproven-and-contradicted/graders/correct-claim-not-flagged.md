---
type: llm
focus: last_message
criteria: |
  "`read_contacts` splits the file into lines (fixtures/parser.py:8), then
  splits each line on commas (fixtures/parser.py:11)" is correct:
  `splitlines()` then `line.split(",")`. It makes no claim about what the
  function does on an empty file.

  PASS if no finding targets that claim.
  FAIL if it is reported as unproven, contradicted, or an over-reaching
  conclusion.
weight: 1
---

A correct, sourced claim is not a finding.

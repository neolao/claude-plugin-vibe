---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or TEST SCENARIOS defines the behaviour of a new
  flag in at least one concrete respect: the response to an unknown
  `--status` value (a usage error with a non-zero exit code, not an empty
  table or a silent ignore), or what `--json` prints when no backup matches
  (an empty array, still valid JSON), or that `--json` output goes to
  stdout with nothing else mixed in.
  FAIL if the new flags' behaviour is never defined beyond "add a status
  filter and a JSON output", or if an unknown status value is said to print
  the unfiltered table.
weight: 1
---

Defines the new flags — the unknown-value case, the empty-result case or
the stdout contract of `--json` — instead of spending the lists on a
transition that is not needed.

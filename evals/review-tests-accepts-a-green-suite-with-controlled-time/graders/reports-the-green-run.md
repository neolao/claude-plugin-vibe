---
type: llm
focus: last_message
criteria: |
  `python3 -m unittest discover -s fixtures -v` runs 6 tests, all
  passing.

  PASS if the `SUITE EXECUTED:` line reports the run as PASS (or an
  equivalent word) with 6 passed and nothing failed.
  FAIL if the line reports a failure, an error, or NOT RUN.
weight: 1
---

Reports the real result of the run: green, six tests.

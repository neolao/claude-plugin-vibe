---
type: llm
focus: last_message
criteria: |
  The sub-agent's tool calls are not in the trace; judge on its
  `## IMPLEMENTATION report`. Under **Commands run**, the test command must
  appear at least twice: first with a **failure** (the new over-removal test, run
  before the correction — a failed assertion or an unexpected non-raise), then with a **pass**.

  PASS if the report shows a failing run before a passing run, each with
  its exact result (not "tests pass").
  FAIL if only passing runs are listed, if no command is listed, or if the
  results are paraphrased without the command's own output.
weight: 2
---

Red before green, proven by the commands and their results.

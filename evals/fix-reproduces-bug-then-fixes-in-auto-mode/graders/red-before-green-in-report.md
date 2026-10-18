---
type: llm
focus: trace
criteria: |
  The implementer's tool calls are not in the trace; its `## IMPLEMENTATION
  report` is (as the Agent tool's result). Judge the red step on that report:
  its **Commands run** list must show the test command run with a **failure**
  (the new test, before the code) and then run again with a **pass**.

  PASS if the report shows a failing run before a passing run of the test
  command, and the workflow then re-ran the test command itself (a `Bash`
  call with the test command after the Agent call).
  FAIL if the report shows only passing runs, no commands at all, or the
  workflow trusted the report without re-running the tests.
weight: 2
---

Red before green, read from the implementer's report, confirmed by the
workflow's own re-run.

---
type: llm
focus: last_message
criteria: |
  Every test passes in the run.

  PASS if no finding (a `FILE:` block) carries the category `Failing
  test` or a clearly equivalent one (`Failing`, `Red test`), and no
  finding claims a test failed or errored in the run. A report with no
  findings at all passes.
  FAIL if any finding reports a test as failing in the run.
weight: 2
---

Invents no failing test on a green suite.

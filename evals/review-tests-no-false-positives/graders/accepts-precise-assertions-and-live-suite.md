---
type: llm
focus: last_message
criteria: |
  Every assertion is a precise `assertEqual`/`assertRaises`, no test is
  skipped or commented out, and nothing depends on unavailable
  infrastructure.

  PASS if no `high` or `medium` severity Assertion precision, Dead test
  code, or Infrastructure finding is reported. A `SUITE EXECUTED` header
  confirming the suite passed is expected and is not a finding.
  FAIL if any of the three is reported.
weight: 1
---

Invents no imprecise assertion, dead test, or infrastructure gap in a clean, passing suite.

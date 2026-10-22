---
type: llm
focus: last_message
criteria: |
  "The wait after each failed attempt doubles each time
  (fixtures/sync.py:16)" is
  correct: `time.sleep(2 ** attempt)` waits 1, 2, then 4 seconds.

  PASS if no finding targets that claim.
  FAIL if it is reported as unproven, contradicted or an over-reaching
  conclusion.
weight: 1
---

A correct, sourced claim is not a finding.

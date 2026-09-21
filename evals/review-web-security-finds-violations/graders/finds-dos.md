---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `DoS` (or clearly equivalent
  category name) finding on `report` in fixtures/app.py, for generating a
  report with an attacker-controlled `rows` count and no cap or rate limit,
  allowing an unbounded/expensive operation.
  FAIL if no finding flags `report`'s uncapped `rows` parameter.
weight: 1
---

Reports `report`'s uncapped, client-controlled `rows` parameter as a `DoS`
finding.

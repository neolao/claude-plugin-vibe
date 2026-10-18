---
type: llm
focus: last_message
criteria: |
  "The read timeout is set to 30 seconds (fixtures/parser.py:3)": line 3
  reads `TIMEOUT_SECONDS = 60`.

  PASS if a `(contradicted)` finding quotes the claim and states the source
  value 60.
  FAIL if the claim is accepted or the finding does not give the real value.
weight: 2
---

A wrong figure with a correct citation is still a contradicted claim.

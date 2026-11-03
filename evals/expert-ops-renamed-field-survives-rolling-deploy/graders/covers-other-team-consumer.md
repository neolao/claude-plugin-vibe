---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS names the nightly finance
  reconciliation job (or "the other team's job", "the reporting consumer") and
  says it must keep working on the new messages: the field it reads stays
  available, or its owner is told and migrates before the old field is
  removed.
  FAIL if the reply covers only the tracking service, or never mentions the
  finance reconciliation job.
weight: 2
---

Names the finance reconciliation job and requires it to keep working on the
new messages.

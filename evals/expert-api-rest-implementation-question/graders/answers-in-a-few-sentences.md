---
type: llm
focus: last_message
criteria: |
  This is the implementation-time format — a few sentences — not the plan-time
  three-list format and not a generic API checklist.

  PASS if the reply is a short prose answer to the question asked.
  FAIL if it returns `REQUIREMENTS:` / `RISKS:` / `TEST SCENARIOS:` lists, a
  general checklist of REST advice, or otherwise answers beyond the question
  about the repeated cancel call.
weight: 1
---

Answers in the short implementation-time format, not the plan-time lists.

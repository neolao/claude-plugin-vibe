---
type: llm
focus: last_message
criteria: |
  Finding 4 (review-naming, `exc` could be named `error`) is a matter of
  form: its agent suggested severity high, but the level measures the
  consequence for whoever uses the code, not the severity the agent
  suggested.

  PASS if finding 4 is kept under `## CLASSIFIED findings` at level `low`,
  or dropped under `## DISCARDED` with a reason anchored in the code
  (the name is already conventional or harmless).
  FAIL if it is kept at `medium` or `high`.
weight: 2
---

The classifier re-levels by consequence and does not inherit the agent's
suggested severity.

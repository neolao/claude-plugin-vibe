---
type: llm
focus: last_message
criteria: |
  Every file in the fixture directory uses snake_case; no camelCase or
  kebab-case file sits alongside them.

  PASS if no `high` or `medium` severity Module finding claims the file
  naming is mixed or inconsistent.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not invent inconsistency in uniformly snake_case file names.

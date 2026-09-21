---
type: llm
focus: last_message
criteria: |
  `MAX_RETRIES = 3` is a module-level constant that is never reassigned
  anywhere in the fixtures.

  PASS if no `high` or `medium` severity Mutable global state finding
  targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a never-reassigned constant mutable global state.

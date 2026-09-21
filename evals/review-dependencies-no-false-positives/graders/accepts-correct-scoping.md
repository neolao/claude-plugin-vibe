---
type: llm
focus: last_message
criteria: |
  Every declared dependency is imported somewhere in fixtures/, and `jest`
  is a devDependency used only by fixtures/test/, never by runtime code.

  PASS if no `high` or `medium` severity Unused or Misplaced finding targets
  any of the four packages.
  FAIL if any is flagged at high or medium severity.
weight: 1
---

Does not call correctly scoped, actually-imported dependencies unused or misplaced.

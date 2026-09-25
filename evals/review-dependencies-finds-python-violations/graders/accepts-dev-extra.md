---
type: llm
focus: last_message
criteria: |
  `freezegun` is declared in the `dev` optional-dependencies extra of
  fixtures/pyproject.toml and imported only by fixtures/tests/: it is
  correctly placed.
  PASS if no `high` or `medium` severity `Unused` or `Misplaced` finding
  targets `freezegun`.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not flag a test-only package declared in a dev extra.

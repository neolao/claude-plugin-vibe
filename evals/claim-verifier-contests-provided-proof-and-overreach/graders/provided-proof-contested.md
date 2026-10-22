---
type: llm
focus: last_message
criteria: |
  "All 3 tests pass" is backed by a command output the caller provided
  ("Ran 3 tests ... OK"), but fixtures/test_sync.py defines 2 tests.

  PASS if a finding quotes that claim and flags it as `(contradicted)`,
  saying the test file holds 2 tests while the output announces 3.
  FAIL if the claim is accepted because output was provided, or if it is
  flagged as having no proof at all.
weight: 2
---

A provided proof is contested when the cited source contradicts it.

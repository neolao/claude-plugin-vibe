---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Misplaced` finding on
  `pytest`, declared in `[project] dependencies` of
  fixtures/pyproject.toml although only fixtures/tests/ imports it, with a
  suggestion to move it to a dev/test extra or group.
  FAIL if this is not flagged.
weight: 1
---

Reports the runtime-declared, test-only `pytest` as a Misplaced finding.

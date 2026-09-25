---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Version hygiene` finding on
  `flask>=1.0` in fixtures/pyproject.toml, for its open-ended `>=` range
  on a production dependency with no lockfile committed.
  FAIL if the `flask>=1.0` range is not flagged.
weight: 1
---

Reports `flask>=1.0`'s open-ended range as a Version hygiene finding.

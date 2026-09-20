---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Type` (or clearly equivalent
  category name) finding on the `UserManager` class in fixtures/userManager.py,
  for the vague `Manager` suffix that carries no qualifier about what it
  actually does.
  FAIL if no finding flags `UserManager`'s name for this reason.
weight: 1
---

Reports `UserManager`'s vague `Manager` suffix as a `Type` finding.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Misplaced` finding on `express`
  in fixtures/package.json, for being declared under `devDependencies` while
  fixtures/src/index.js requires it at runtime to start the server — a
  production dependency misplaced as dev-only.
  FAIL if this mismatch is not flagged.
weight: 1
---

Reports `express` declared as a devDependency but required at runtime as a
Misplaced finding.

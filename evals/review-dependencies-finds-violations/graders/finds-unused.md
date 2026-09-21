---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Unused` finding on the `uuid`
  dependency declared in fixtures/package.json, noting it is never required
  or imported anywhere in fixtures/src/ or fixtures/test/.
  FAIL if `uuid` is not flagged as unused/never imported.
weight: 1
---

Reports the declared-but-never-imported `uuid` dependency as an Unused
finding.

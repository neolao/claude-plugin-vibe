---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Abandoned` finding on the
  `request` package declared in fixtures/package.json, noting it is
  deprecated/no longer maintained and suggesting a replacement such as
  `fetch`, `undici`, or `node-fetch`.
  FAIL if `request` is not flagged as abandoned/deprecated.
weight: 1
---

Reports the deprecated `request` package as an Abandoned finding.

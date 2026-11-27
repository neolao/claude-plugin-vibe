---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md links to `troubleshooting.md` ("the
  troubleshooting page"); no such file exists under fixtures/docs/ or
  anywhere in the fixture.

  PASS if the reported findings include a `Dangling reference` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/docs/import.md and that names `troubleshooting.md` (or the
  troubleshooting link) as the target that does not exist.
  FAIL if no finding reports that link.
weight: 2
---

Reports the relative link whose target file does not exist.

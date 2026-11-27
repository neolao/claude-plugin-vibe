---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md says a parsed statement is kept in
  `.ledger/cache/`, "created on first run"; no such directory exists in
  the fixture.

  PASS if no `high` or `medium` severity finding names `.ledger/cache/`
  as a dangling reference, a broken path or any other defect. A `low`
  finding passes, and so does a report with no findings at all.
  FAIL if `.ledger/cache/` is flagged at high or medium severity.
weight: 2
---

Does not report a path the doc says the tool creates at runtime: it is
absent from the repository by design.

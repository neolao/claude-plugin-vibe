---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md shows `ledger import path/to/statement.csv`,
  `ledger import statements/*.csv` and names exports
  `exports/<period>.xlsx`: a placeholder path, a glob and a name pattern
  inside examples, none presented as a file that exists in the
  repository.

  PASS if no `high` or `medium` severity finding names
  `path/to/statement.csv`, `statements/*.csv` or `exports/<period>.xlsx`
  as a dangling reference, a broken path or any other defect. A `low`
  finding passes, and so does a report with no findings at all.
  FAIL if any of those three is flagged at high or medium severity.
weight: 2
---

Does not report a placeholder, a glob or a name pattern as a path that
resolves nowhere: an example path is not a citation.

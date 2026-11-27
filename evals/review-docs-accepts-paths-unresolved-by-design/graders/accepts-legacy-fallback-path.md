---
type: llm
focus: last_message
criteria: |
  fixtures/docs/configuration.md says the legacy `ledger.ini` is still
  read when `ledger.toml` is absent; fixtures/ledger.toml exists and no
  ledger.ini does.

  PASS if no `high` or `medium` severity finding names `ledger.ini` as a
  dangling reference, a broken path or any other defect. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if `ledger.ini` is flagged at high or medium severity.
weight: 2
---

Does not report a path the doc itself calls legacy and a fallback: the
doc says it may be absent, and it is.

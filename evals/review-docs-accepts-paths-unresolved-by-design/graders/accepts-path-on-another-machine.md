---
type: llm
focus: last_message
criteria: |
  fixtures/docs/configuration.md locates the server inbox at
  `/var/lib/ledger/inbox/` and the done directory at
  `/var/lib/ledger/done/`: absolute paths on the server, not files of the
  repository.

  PASS if no `high` or `medium` severity finding names
  `/var/lib/ledger/inbox/` or `/var/lib/ledger/done/` as a dangling
  reference, a broken path or any other defect. A `low` finding passes,
  and so does a report with no findings at all.
  FAIL if either server path is flagged at high or medium severity.
weight: 2
---

Does not report a path that lives on another machine: nothing in the
repository is expected to resolve it.

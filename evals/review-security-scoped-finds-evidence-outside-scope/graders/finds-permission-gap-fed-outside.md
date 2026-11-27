---
type: llm
focus: last_message
criteria: |
  `ALLOWED` in fixtures/archiver/lib/perms.py has a `restore_archive` key
  but no `restore` key, and `require` lets an action absent from the table
  through; `restore` in fixtures/archiver/commands.py, outside the scope,
  calls `perms.require(user, "restore")`, so any staff member, including
  the default `viewer` role, can restore a partner archive into
  /srv/documents.

  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/archiver/lib/perms.py, that names the missing `restore` key or
  the lookup that lets unknown actions through, and whose ISSUE or
  SUGGESTION names `commands.restore` or the `"restore"` action it checks.
  FAIL if no finding reports this gap, or if the finding is anchored (its
  FILE: line) on fixtures/archiver/commands.py.
weight: 1
---

Reports the permission table in scope, with the outside caller's action
name as the evidence that the check cannot bind.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name) finding for `restore` not being restricted to
  admins: `commands.restore` (fixtures/archiver/commands.py) calls
  `perms.require(user, "restore")`, but `ALLOWED`
  (fixtures/archiver/perms.py) only holds a `"restore_archive"` key, and
  `require` lets any action it has no entry for through, so an operator or a
  viewer can restore archives. The finding may be anchored in perms.py or
  commands.py, as long as it says `restore` is not actually checked (the key
  mismatch, the permissive default, or both).
  FAIL if no finding flags this missing check.
weight: 1
---

Reports `"restore"` missing from `ALLOWED` and `require` allowing it anyway.
commands.py alone checks a permission; only perms.py shows the check never
matches.

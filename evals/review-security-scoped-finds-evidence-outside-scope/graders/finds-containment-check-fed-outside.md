---
type: llm
focus: last_message
criteria: |
  `inside` in fixtures/archiver/lib/paths.py checks `target.startswith(root)`
  on the result of `os.path.join` without normalizing it
  (`realpath`/`abspath`/`resolve`); `restore` in fixtures/archiver/
  commands.py, outside the scope, passes it each `entry.name` of the
  listing that fixtures/archiver/manifest.py reads from the partner's
  archive, so a name like `../../etc/cron.d/job` passes the check and is
  written wherever the partner's manifest says.

  PASS if the reported findings include an `Injection` (or clearly
  equivalent category name, such as path traversal or Trust boundary)
  finding whose FILE: line points to fixtures/archiver/lib/paths.py, that
  names the containment check letting `..` through for want of
  normalization, and whose ISSUE or SUGGESTION names `restore`, the
  manifest entries or the partner's archive as where the names come from.
  FAIL if no finding reports this containment check, or if the finding is
  anchored (its FILE: line) on fixtures/archiver/commands.py or
  fixtures/archiver/manifest.py.
weight: 1
---

Reports the containment check in scope, with the outside manifest reader
as the evidence that the names are the partner's.

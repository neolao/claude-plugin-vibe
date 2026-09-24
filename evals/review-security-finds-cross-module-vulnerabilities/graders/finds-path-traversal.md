---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Injection` (or clearly
  equivalent category name, such as path traversal) finding for the restore
  target path: `paths.inside` (fixtures/archiver/paths.py) checks
  `target.startswith(root)` on the result of `os.path.join` without
  normalizing it (`realpath`/`abspath`/`resolve`), so an `entry.name` like
  `../../etc/cron.d/job` passes the check, and `restore`
  (fixtures/archiver/commands.py) writes it wherever the partner's manifest
  says. The finding may be anchored in paths.py or commands.py, as long as it
  names the containment check that lets `..` through.
  FAIL if no finding flags this traversal.
weight: 1
---

Reports `paths.inside` letting `..` through because it never normalizes.
commands.py alone calls a containment helper; only paths.py shows the check
is on the raw joined string.

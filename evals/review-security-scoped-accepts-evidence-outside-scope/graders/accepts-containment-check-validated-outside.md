---
type: llm
focus: last_message
criteria: |
  `inside` in fixtures/archiver/lib/paths.py checks `target.startswith(root)`
  on the result of `os.path.join` without normalizing it. Its only caller,
  `restore` in fixtures/archiver/commands.py (outside the scope), passes it
  the entry names that `read` in fixtures/archiver/manifest.py accepted
  against `^[A-Za-z0-9][A-Za-z0-9._-]{0,127}$`, which rejects `..`, `/`
  and any name starting with a dot: no name that could leave the root
  reaches the check.

  PASS if no `high` or `medium` severity `Injection`, path traversal or
  `Trust boundary` (or clearly equivalent category name) finding targets
  `inside` or its `startswith` check. A `low` finding passes, and so does
  a report with no findings at all.
  FAIL if the containment check is reported as letting `..` through, or as
  a traversal, at high or medium severity.
weight: 1
---

Does not call a containment check a traversal when the names it receives
are validated outside the scope.

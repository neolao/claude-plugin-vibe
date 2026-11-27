---
type: llm
focus: last_message
criteria: |
  `ALLOWED` in fixtures/archiver/lib/perms.py carries the four actions the
  commands in fixtures/archiver/commands.py check (`pack`, `restore`,
  `share`, `rotate_key`), and `require` raises `Forbidden` for an action
  absent from the table as well as for a role not listed.

  PASS if no finding claims that an action the commands check is missing
  from the table, or that `require` lets unknown actions through. A report
  with no findings at all passes.
  FAIL if an `Access control` (or clearly equivalent category name)
  finding targets `ALLOWED` or `require`.
weight: 1
---

Does not invent a gap in a permission table that holds every action its
outside callers check.

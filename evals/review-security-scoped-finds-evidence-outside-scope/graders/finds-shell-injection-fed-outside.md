---
type: llm
focus: last_message
criteria: |
  `run_tool` in fixtures/archiver/lib/proc.py joins its tool and arguments
  into one string and runs it with `shell=True`; `restore` in
  fixtures/archiver/commands.py, outside the scope, passes it
  `archive_path`, the CLI argument of `archiver restore`, which the README
  says is a file name the partner site chose when uploading into
  /srv/inbox — a name holding `;` or `$(...)` runs as a command under the
  staff member's account.

  PASS if the reported findings include an `Injection` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/archiver/lib/proc.py, that names the `shell=True` call on a
  joined string, and whose ISSUE or SUGGESTION names `restore`,
  fixtures/archiver/commands.py, the archive path or the partner-chosen
  file name as what makes the input external. The fix direction should be
  an argument list without a shell (`run_argv` or equivalent).
  FAIL if no finding reports this shell call, or if the finding is
  anchored (its FILE: line) on fixtures/archiver/commands.py or
  fixtures/archiver/cli.py.
weight: 2
---

Reports the shell helper in scope as Injection once its outside caller
shows it is fed a partner-chosen name: proc.py alone shows a helper with
no caller.

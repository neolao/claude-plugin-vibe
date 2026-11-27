---
type: llm
focus: last_message
criteria: |
  `run_tool` in fixtures/archiver/lib/proc.py joins its tool and arguments
  into one string and runs it with `shell=True`. Its only caller, `pack` in
  fixtures/archiver/commands.py (outside the scope), passes it `"gpg"` and
  `["--batch", "--detach-sign", dest]`, where `dest` is the outbox folder
  plus today's date: nothing a partner, a customer or a CLI argument
  chooses reaches the string. `restore` runs tar through `run_argv`, an
  argument list without a shell.

  PASS if no `high` or `medium` severity `Injection` or `Dangerous
  primitive` (or clearly equivalent category name) finding targets
  `run_tool` or its `shell=True` call. A `low` finding passes, and so does
  a report with no findings at all.
  FAIL if the shell call is reported as injectable or reachable by external
  input at high or medium severity.
weight: 2
---

Does not call a shell helper injectable when its only caller, outside the
scope, feeds it constants.

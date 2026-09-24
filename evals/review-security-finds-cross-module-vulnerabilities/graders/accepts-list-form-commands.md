---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags `proc.run_argv` (fixtures/archiver/proc.py) or
  the `tar`/`gpg` calls in `pack` (fixtures/archiver/commands.py) as a
  command or shell injection. `run_argv` passes a list to `subprocess.run`
  without `shell=True`.
  A finding on `run_tool` or on `restore` does not count against this
  grader, even if it points at `run_argv` as the fix. Neither does a report
  that mentions `run_argv` only to say it is safe.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the list-form `run_argv` calls in `pack`.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `Injection` (or clearly
  equivalent category name) finding for the shell command built in
  `restore`: `commands.restore` (fixtures/archiver/commands.py) passes
  `archive_path` to `proc.run_tool`, which (fixtures/archiver/proc.py) joins
  the arguments into one string and runs it with `shell=True`. The archive
  file name is chosen by the partner site that uploaded it, so a name
  containing `;` or `$(...)` runs commands as the staff account. The finding
  may be anchored in proc.py or commands.py, as long as it names this path
  from the archive name to the shell.
  FAIL if no finding flags this shell injection.
weight: 1
---

Reports the partner-chosen archive name reaching `shell=True` through
`run_tool`. commands.py alone passes a list; only proc.py shows it becomes a
shell string.

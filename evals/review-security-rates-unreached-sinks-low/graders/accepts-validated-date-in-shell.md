---
type: llm
focus: last_message
criteria: |
  `ingest` in fixtures/importer.py concatenates `day` into a `shell=True`
  command after `datetime.strptime(day, "%Y-%m-%d")`, which raises on
  anything but digits and dashes in that layout; the README says the
  uploads are stored under that date name by the SFTP server, not under a
  name the supplier chooses. Nothing a supplier or an operator writes
  reaches the shell unchanged.

  PASS if no `high` or `medium` severity `Injection` (or clearly
  equivalent category name) finding targets the `unzip` command. A `low`
  finding passes, and so does a report with no findings at all.
  FAIL if the command is reported as injectable at high or medium
  severity.
weight: 2
---

Does not rate a shell command above low when the only value reaching it
is validated as a date first.

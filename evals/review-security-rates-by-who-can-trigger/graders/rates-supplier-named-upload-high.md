---
type: llm
focus: last_message
criteria: |
  `ingest` in fixtures/importer.py concatenates `upload_path` into a
  `shell=True` command; the README says the path is the upload a supplier
  made over SFTP, under a file name the supplier chose. An outsider
  triggers the injection with nothing more than the upload the tool
  already accepts.

  PASS if the reported findings include an `Injection` (or clearly
  equivalent category name) finding on this `unzip` command with
  `SEVERITY: high`.
  FAIL if no finding reports the command, or if it is rated `medium` or
  `low`.
weight: 2
---

Rates a sink an outsider reaches through what the entry point already
accepts high.

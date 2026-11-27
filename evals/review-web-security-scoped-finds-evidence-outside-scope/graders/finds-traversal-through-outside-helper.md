---
type: llm
focus: last_message
criteria: |
  `download` in fixtures/portal/routes/files.py serves
  `storage.upload_path(name)` for a `<path:name>` any visitor types;
  `upload_path` in fixtures/portal/storage.py, outside the scope, is a bare
  `os.path.join(UPLOAD_DIR, name)` with no normalization and no check that
  the result stays under the upload directory, so a name holding `..`
  segments reads any file the server account can open.

  PASS if the reported findings include a `Path traversal` (or clearly
  equivalent category name) finding whose FILE: line points to
  fixtures/portal/routes/files.py, and whose ISSUE or SUGGESTION names
  `upload_path`, fixtures/portal/storage.py or the join without
  containment as what lets the name escape.
  FAIL if no finding reports this download, or if the finding is anchored
  (its FILE: line) on fixtures/portal/storage.py.
weight: 2
---

Reports the route in scope as Path traversal once the outside helper
shows the join is unchecked: files.py alone shows a helper call.

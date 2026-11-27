---
type: llm
focus: last_message
criteria: |
  `download` in fixtures/portal/routes/files.py serves
  `storage.upload_path(name)`; `upload_path` in fixtures/portal/storage.py,
  outside the scope, resolves the joined path with `os.path.realpath` and
  raises unless it still starts with the upload directory plus a
  separator, so no name reaches a file outside it.

  PASS if no `high` or `medium` severity `Path traversal` (or clearly
  equivalent category name) finding targets `download` or `upload_path`.
  A `low` finding passes, and so does a report with no findings at all.
  FAIL if the download is reported as escaping the upload directory at
  high or medium severity.
weight: 2
---

Does not call a route a traversal when the helper outside the scope
contains the name.

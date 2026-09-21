---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Path traversal` (or clearly
  equivalent category name) finding on `download_file` in
  fixtures/app.py, for joining the user-supplied `filename` into
  `UPLOAD_DIR` with no normalization or check that the resolved path stays
  inside the upload directory.
  FAIL if no finding flags `download_file`'s unvalidated path join.
weight: 1
---

Reports `download_file`'s unvalidated path join as a `Path traversal`
finding.

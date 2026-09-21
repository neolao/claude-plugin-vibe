---
type: llm
focus: last_message
criteria: |
  `download_file` sanitizes the name with `secure_filename` and re-checks
  that the resolved real path still sits inside `UPLOAD_DIR` before serving.

  PASS if no `high` or `medium` severity Path traversal finding targets it.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a containment-checked file read a traversal.

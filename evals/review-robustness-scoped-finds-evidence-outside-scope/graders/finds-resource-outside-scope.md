---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Resource` (or clearly equivalent
  category name) finding on `dispatch_parcel` (fixtures/shipping/dispatch.py)
  for closing the label outside a `with` or `try`/`finally`: `labels.open_for`
  (fixtures/spool/labels.py) returns a file opened for writing, so when
  `render_label` or the write raises (a parcel missing a field, a full spool
  disk), `label.close()` is skipped and the handle and a partial label file
  are left behind.
  FAIL if no finding flags this unguarded open/close in `dispatch_parcel`.
weight: 1
---

Reports the label handle returned by `labels.open_for` and closed outside a
`finally` in `dispatch_parcel`. dispatch.py alone shows a returned object;
only spool/labels.py, outside the scope, shows it is an open file.

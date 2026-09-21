---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Resource` (or clearly equivalent
  category name) finding on `export_orders` in
  fixtures/export_writer.py, for opening the file with a bare `open(path,
  "w")` and closing it with an explicit `f.close()` at the end instead of a
  `with`/try-finally — so an exception raised while writing a row leaves the
  file handle open and a partial file on disk.
  FAIL if no finding flags the unguarded `open`/`close` in `export_orders`.
weight: 1
---

Reports the `open`/`close` without a `with` or try-finally guard in
`export_orders` as a `Resource` finding.

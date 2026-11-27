---
type: llm
focus: last_message
criteria: |
  fixtures/docs/guides/export.md links to `../reference/encoding.md`
  ("the encoding reference"); no such file exists under
  fixtures/docs/reference/.

  PASS if the reported findings include a `Dangling reference` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/docs/guides/export.md and that names `encoding.md` (or the
  "encoding reference" link) as the target that does not exist.
  FAIL if no finding reports that link.
weight: 2
---

Reports the broken link of the in-scope guide: the anchor that depends
on no outside doc, only on the file system.

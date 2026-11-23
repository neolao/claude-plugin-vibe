---
type: llm
focus: last_message
criteria: |
  In fixtures/billing/invoicer.py, `Invoicer.__init__` receives its
  `repository` as a parameter and builds `PdfRenderer()` by hand, under a
  comment explaining that the renderer holds the lines of the document being
  drawn and that the objects app.py builds at start-up are shared by every
  request thread.

  Only a finding counts: a block with a `FILE:` line. A sentence outside any
  finding (for example one saying the renderer was considered and left
  alone) passes.
  PASS if no finding asks for `PdfRenderer` to be injected into `Invoicer`
  or calls its hand-construction a half-done migration, a leftover or an
  inconsistency. A report with no finding on fixtures/billing/invoicer.py
  passes.
  FAIL if any finding flags the hand-built `PdfRenderer` of `Invoicer`.
weight: 1
---

Leaves alone an object built by hand next to an injected dependency when a
comment states a reason that still holds for keeping it there.

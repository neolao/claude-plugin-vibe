---
type: llm
focus: last_message
criteria: |
  fixtures/docs/export.md says "the reconciliation is written to
  `exports/` ... send that file to the accountant": .vibe/glossary.md
  defines that file as the Export and, under both Reconciliation and
  Export, says not to confuse the two.

  PASS if the reported findings include a `Vocabulary` (or clearly
  equivalent category name) finding, whatever its severity, whose FILE:
  line points to fixtures/docs/export.md and that says "reconciliation"
  is used there for what the glossary calls the Export (naming the
  glossary, the Export entry or its "do not confuse with" line).
  FAIL if no finding reports that use of "reconciliation", or if the
  finding rests on no glossary entry.
weight: 2
---

Reports the passage that names Reconciliation while describing the file
written for the accountant.

---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md says to "download the invoice from your bank's
  website" and that Ledger "parses the invoice into transactions":
  .vibe/glossary.md defines that file as a Statement and says, under
  both Statement and Invoice, not to confuse the two.

  PASS if the reported findings include a `Vocabulary` (or clearly
  equivalent category name) finding, whatever its severity, whose FILE:
  line points to fixtures/docs/import.md and that says "invoice" is used
  there for what the glossary calls a Statement (naming the glossary, the
  Statement entry or its "do not confuse with" line).
  FAIL if no finding reports that use of "invoice", or if the finding
  rests on no glossary entry.
weight: 2
---

Reports the passage that names Invoice while describing the bank's file,
resting on the glossary's own "do not confuse with" arbitration.

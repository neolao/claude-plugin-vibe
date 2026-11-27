---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md uses "statement" for the bank's file,
  "invoice" for what a transaction is matched with and "reconciliation"
  for the matching; fixtures/docs/export.md uses "export" for the file
  sent to the accountant and "reconciliation" for the matching it reads.
  Each use matches its .vibe/glossary.md entry.

  PASS if no `high` or `medium` severity finding says that "statement",
  "invoice", "reconciliation" or "export" is used for another glossary
  term, confused with another term or non-canonical. A `low` finding
  passes, and so does a report with no findings at all.
  FAIL if any of those four terms is flagged at high or medium severity
  as confused or non-canonical.
weight: 2
---

Does not report a term used in the sense its entry gives it, nor a
"do not confuse with" term used in its own sense.

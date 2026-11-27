---
type: llm
focus: last_message
criteria: |
  fixtures/docs/import.md says "the statement (what your bank's website
  may call an account export)" once, and never uses "account export"
  again.

  PASS if no `high` or `medium` severity finding names "account export"
  as a non-canonical spelling, a second name for Statement or any other
  vocabulary defect. A `low` finding passes, and so does a report with no
  findings at all.
  FAIL if "account export" is flagged at high or medium severity.
weight: 2
---

Does not report a synonym used once to teach the canonical term.

---
type: llm
focus: last_message
criteria: |
  "bank file" appears only in fixtures/docs/history.md, inside a line
  recording the 2025 rename and quoting the 2024 release notes, and in
  the code identifier `parse_bank_file()` of fixtures/docs/export.md;
  `invoice not found` in fixtures/docs/import.md is a verbatim error
  message.

  PASS if no `high` or `medium` severity finding names "bank file",
  `parse_bank_file()` or `invoice not found` as a vocabulary defect. A
  `low` finding passes, and so does a report with no findings at all.
  FAIL if any of the three is flagged at high or medium severity.
weight: 2
---

Does not report historical or quoted text, a code identifier or a
verbatim error message: that wording is a fact of the archive or of the
code, not a choice the author makes now.

---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Fixture` (or clearly equivalent
  category name — a `Coverage gap` counts when it names the `SAMPLE`
  fixture's triviality as the cause) finding on the `SAMPLE` constant used
  by fixtures/test_user_import.py, for being a single unquoted row with no
  blank line, so none of `parse_users`' real parsing branches (blank-line
  skip, whitespace strip, quote strip, a name containing a comma) is ever
  exercised.
  FAIL if no finding flags `SAMPLE` as too trivial to exercise the parser.
weight: 1
---

Reports the one-row `SAMPLE` import fixture as a `Fixture` finding.

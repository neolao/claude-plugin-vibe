---
type: llm
focus: last_message
criteria: |
  Two facts are in the sources and must not reach the Product Owner as
  questions:
  - the export format and its columns (CSV; date, amount, label) —
    acceptance criterion 1 of the backlog item;
  - who "admins" are — `.vibe/decisions/002` and the index's observed
    pattern: the `owner` role only, `member` is read-only.

  PASS if no question in any round (an `AskUserQuestion` question or a `❓`
  question) asks which format to use, which
  columns to include, or which roles may export / who the admins are.
  FAIL if any round asks one of those.
weight: 3
---

The Product Owner is asked only what no source answers.

---
type: llm
focus: last_message
criteria: |
  Item 002 has `depends_on: [001, 009]`. Item 001 exists with `status: todo`;
  no item 009 exists anywhere.

  PASS if the 002 row (or its surrounding text) lists 001 as an unmet
  dependency without calling it missing, unknown or non-existent — only 009
  may carry that label.
  FAIL if 001 is labelled missing (or equivalent), or if 001 is not shown as
  an unmet dependency of 002 at all.
weight: 2
---

Precision inside the same row: an unmet dependency that exists is shown the
ordinary way, the "missing" label is reserved for the number with no file.

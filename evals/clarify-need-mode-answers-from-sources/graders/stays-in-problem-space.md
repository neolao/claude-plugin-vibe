---
type: llm
focus: last_message
criteria: |
  The `need` mode decides what the product does, never how it is built.

  PASS if no question and no decision in the report is about code: no file
  or module placement, no library, no function name, no test strategy, no
  "where does the export live".
  FAIL if any such solution-space point is asked or settled in this mode.
weight: 1
---

Stays in the problem space; the implementation mode comes next.

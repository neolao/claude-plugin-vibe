---
type: llm
focus: last_message
criteria: |
  The `need` mode decides what the product does, never how it is built.

  PASS if no question and no decision in the report is about code: no file
  or module placement, no library, no function name, no test strategy, no
  "where does the export live" in the code. Where the user finds the
  export in the product (the admin page, as the backlog item says) is a
  product point. A line under `### Other space` that leaves a point to the
  implementation mode without settling it is not a decision.
  FAIL if any such solution-space point is asked or settled in this mode.
weight: 1
---

Stays in the problem space; the implementation mode comes next.

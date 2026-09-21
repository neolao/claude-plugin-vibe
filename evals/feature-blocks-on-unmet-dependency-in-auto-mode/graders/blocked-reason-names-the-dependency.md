---
type: llm
focus: last_message
criteria: |
  Item 002 declares `depends_on: [001]`, and 001 is still `status: todo`.

  PASS if the reason on the `AUTO-RESULT: blocked` line (or the report right
  above it) says the run stopped because item 001 is not done.
  FAIL if the reason is generic, names a different cause, or names a
  different item.
weight: 2
---

Names 001 as the unmet dependency in the blocked reason.

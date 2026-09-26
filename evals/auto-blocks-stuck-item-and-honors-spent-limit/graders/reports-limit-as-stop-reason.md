---
type: llm
focus: last_message
criteria: |
  The run stops because its limit of 3 items is used up (001, 002, and 003,
  which was just blocked), while item 004 is still eligible.

  PASS if the final report says the run stopped because the limit was
  reached (or spent, or exhausted).
  FAIL if it says the run stopped because no eligible item remained, gives
  no stop reason, or reports having started or shipped 004.
weight: 2
---

Names the spent limit, not an empty backlog, as the reason the run stopped.

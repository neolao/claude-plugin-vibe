---
type: llm
focus: last_message
criteria: |
  PASS if the report tells the user that running `/vibe:feature 002` (or
  `/vibe:fix 002`) puts the blocked item back in play, as Step 2 prescribes.
  FAIL if no such next step is given for the blocked item.
weight: 1
---

Says how to put the blocked item back in play.

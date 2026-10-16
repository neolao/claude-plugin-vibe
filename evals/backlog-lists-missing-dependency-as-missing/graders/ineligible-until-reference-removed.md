---
type: llm
focus: last_message
criteria: |
  Item 002 depends on 009, and no item 009 exists.

  PASS if the final message tells the user that 002 cannot be picked by
  `/vibe:auto` (stays ineligible, will never be selected, or equivalent)
  until 009 is removed from its `depends_on` (edited out of the file, or
  equivalent).
  FAIL if the message only shows the marker in the table with no such
  explanation, or suggests the dependency will resolve on its own.
weight: 2
---

Says what the missing reference means for autonomous runs and how to clear
it, per Step 2.

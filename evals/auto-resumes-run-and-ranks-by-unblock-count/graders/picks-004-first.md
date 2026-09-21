---
type: llm
focus: last_message
criteria: |
  Three items are eligible once the orphan is reset: 003 (a defect, lowest
  number, nothing depends on it), 004 (one other todo item, 005, lists it in
  `depends_on`), and 006 (nothing depends on it). Step 1 ranks by unblock
  count first, defects second, lowest number last — so 004 comes first.

  PASS if the first item this run starts is 004, as shown by its status lines
  or its summary table.
  FAIL if it starts with 003 or 006, i.e. if defect-first or lowest-number
  was applied ahead of the unblock count.
weight: 3
---

Ranks the item others wait on ahead of the lower-numbered defect.

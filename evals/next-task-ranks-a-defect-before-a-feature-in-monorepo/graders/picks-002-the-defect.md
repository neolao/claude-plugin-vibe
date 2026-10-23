---
type: llm
focus: last_message
criteria: |
  Both items are eligible and nothing depends on either, so the unblock
  counts tie at zero. Item 002's title and description use defect
  vocabulary ("crash"); item 001 is a feature. Step 5 ranks defects before
  features ahead of the lowest number.

  PASS if the presented pick is item 002.
  FAIL if it picks item 001 or reports no candidate.
weight: 3
---

Ranks the defect before the lower-numbered feature.

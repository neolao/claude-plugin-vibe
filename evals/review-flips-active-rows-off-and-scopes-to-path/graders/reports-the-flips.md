---
type: llm
focus: last_message
criteria: |
  PASS if the final report names both review-dependencies and review-architecture as rows it switched from active to inactive, with a reason for each.
  FAIL if either flip is missing from the report.
---

Step 1 requires every flipped row to be listed in the report.

---
type: llm
focus: last_message
criteria: |
  PASS if the final message:
  - includes a summary table (or a clearly equivalent structured summary)
    listing the processed backlog item, with a type (feature/fix), a verdict
    (e.g. done/shipped), and something identifying the resulting commit; and
  - explicitly states why the run stopped: because no more eligible backlog
    items remained (not a turn limit, timeout, or error).
  FAIL if the message has no such summary, or does not explain that the run
  stopped for lack of further eligible items.
weight: 1
---

The closing summary (Step 5 of `/vibe:auto`) must include the per-item
summary table and the reason the run ended.

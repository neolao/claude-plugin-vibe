---
type: llm
focus: last_message
criteria: |
  The run was invoked with a limit of 1 on a backlog holding a single
  eligible item, so once that item ships two of Step 4's stop conditions
  hold at once: the limit is reached and no eligible item remains.

  PASS if the final message:
  - includes a summary table (or a clearly equivalent structured summary)
    listing the processed backlog item, with a type (feature/fix), a verdict
    (e.g. done/shipped), and something identifying the resulting commit; and
  - explicitly states why the run stopped, naming the limit being reached,
    the lack of further eligible items, or both.
  FAIL if the message has no such summary, gives no stop reason, or blames
  the stop on a turn limit, a timeout, or an error.
weight: 1
---

The closing summary (Step 5 of `/vibe:auto`) must include the per-item
summary table and the reason the run ended, which Step 4 draws from its stop
conditions.

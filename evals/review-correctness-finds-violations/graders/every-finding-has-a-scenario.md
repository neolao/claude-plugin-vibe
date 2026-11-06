---
type: llm
focus: last_message
criteria: |
  The agent's definition requires a `SCENARIO:` line on every finding:
  the input or state that triggers the bug, the path (entry point or
  caller) that reaches the line, and the wrong output, crash or corrupted
  state.

  PASS if every reported finding carries a `SCENARIO:` line (or a line
  clearly labelled as the failure scenario) that names a concrete
  triggering input or state and what then goes wrong — "an order with
  status unpaid and shipped=False → can_refund returns True", "payments of
  0.1 and 0.2 on a 0.3 invoice → is_settled returns False".
  FAIL if at least one finding has no scenario line, or a scenario that
  states no concrete input or state ("in some cases this fails", "could
  be wrong").
weight: 2
---

Every finding comes with a concrete failure scenario, as the agent's
contract requires; a finding without one should have been dropped.

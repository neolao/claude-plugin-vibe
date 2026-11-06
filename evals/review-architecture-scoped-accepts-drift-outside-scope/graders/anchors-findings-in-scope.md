---
type: llm
focus: last_message
criteria: |
  The scope given to the agent was the two files
  fixtures/core/order_service.py and fixtures/core/pricing.py.

  PASS if every finding's `FILE:` line points to one of those two files
  and no `MODULE:` line names a module other than `core`, or if there is
  no finding at all.
  FAIL if any finding is anchored (`FILE:` or `MODULE:`) on a file or
  module outside the scope.
weight: 1
---

Keeps every finding anchored on a file in scope, or stays silent.

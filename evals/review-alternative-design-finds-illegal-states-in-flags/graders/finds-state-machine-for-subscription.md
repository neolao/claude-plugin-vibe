---
type: llm
focus: last_message
criteria: |
  `Subscription` in fixtures/subscriptions/subscription.py carries
  `is_trial`, `is_active`, `is_paused` and `is_cancelled` as independent
  booleans; fixtures/subscriptions/service.py mutates them from three
  places and `label()` and `can_be_billed()` each re-derive the lifecycle
  from their own flag priority.

  PASS if a finding anchored on fixtures/subscriptions/subscription.py
  proposes an explicit state machine, a sum type / enum of lifecycle states
  with exhaustive matching, or type-state, replacing the boolean flags, and
  its ISSUE or BASELINE says the flags allow contradictory combinations
  (for example paused and cancelled at once) or that the lifecycle is
  re-derived in several places.
  FAIL if no such design is proposed for the flags, or if the finding only
  says the class has too many booleans without naming a design.
weight: 2
---

Finds the lifecycle hidden in boolean flags and names the design that makes
the illegal combinations unrepresentable.

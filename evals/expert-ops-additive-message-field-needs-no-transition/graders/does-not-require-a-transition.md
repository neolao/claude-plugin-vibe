---
type: llm
focus: last_message
criteria: |
  The brief adds one optional field to a message and changes nothing that
  exists: every current field keeps its name, type and meaning, and both
  readers ignore fields they do not know. The expert's own checklist says
  an additive change — an optional field — needs no transition.

  PASS if no REQUIREMENTS entry demands a dual-publish period (the message
  published twice or in two shapes), a new message version or a new topic,
  a feature flag gating the field, a multi-release sequence, or a notice
  to or a change in the finance team's job as a condition of this change.
  Stating that the previous version and both readers keep working during
  the rollout because the field is optional and ignored when unknown, with
  a test scenario for it, is expected and passes; requiring that the
  tracking service treat the field as optional also passes.
  FAIL if REQUIREMENTS requires a dual-publish period, a versioned message
  or topic, a feature flag, a multi-release expand/contract sequence, or a
  change to the finance job as the condition for adding
  `estimated_delivery`.
weight: 2
---

Does not reach for a transition on an additive change: the compatibility
rule triggers on what a running version would feel, and here it feels
nothing.

---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS specifically requires the particle physics
  (gravity/drag simulation) to run on a fixed simulation timestep decoupled
  from the variable render rate, so the effect looks the same at 30 fps and
  144 fps as stated in the brief — not a generic "make it frame-rate
  independent" statement with no mention of separating simulation from
  render rate.
  FAIL if the fixed-timestep / simulation-vs-render-rate separation is
  absent or only stated generically.
weight: 2
---

Requires the particle physics simulation to run at a fixed timestep
decoupled from the variable render rate.

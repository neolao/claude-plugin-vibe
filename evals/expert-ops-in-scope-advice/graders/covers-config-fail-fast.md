---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS says, specifically for the per-account
  webhook signing secret described in the brief (which does not exist
  anywhere yet), that the worker reads it from the environment or a
  secrets store (not hardcoded) and fails fast at startup when it is
  missing, instead of starting without it. Any wording of that refusal
  counts: "fails fast at startup", "refuses to start without it", "the
  process fails to start without it", "exits at startup if unset". Extra
  detail (naming the variable, never logging it) is welcome but not
  required.
  FAIL if the startup fail-fast on this missing secret is absent, or only
  stated as a generic "manage secrets properly" / "use environment
  variables" platitude with no tie to this secret and this worker.
weight: 2
---

Names the startup fail-fast on the webhook secret the brief says does not
exist yet, tailored to this worker.

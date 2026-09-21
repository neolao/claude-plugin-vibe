---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS or RISKS names, specifically for the per-account
  webhook signing secret described in the brief, that it must come from
  environment/config (not hardcoded), that the worker must fail fast at
  startup if it is missing (naming the variable), and that it must never
  appear in logs. A generic "manage secrets properly" or "use environment
  variables" restatement with no tie to this specific secret and this
  specific worker does not count.
  FAIL if the secret-handling/fail-fast concern is absent, or only stated
  as a generic platitude not tailored to the brief.
weight: 2
---

Names the per-account webhook secret's config handling and startup
fail-fast behavior, tailored to this brief.

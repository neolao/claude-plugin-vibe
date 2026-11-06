---
type: llm
focus: last_message
criteria: |
  The two new values default to what production runs with today — a
  30-second timeout and batches of 500 — and exist so the on-call engineer
  can lower them during an incident. The expert's own checklist requires a
  value only when its convenient default would be wrong in production;
  these defaults are the production values.

  PASS if no REQUIREMENTS entry makes the timeout or the batch size a
  required variable, demands they be set explicitly per environment or in
  the production manifest, or has the job fail at startup when they are
  unset. Requiring that an out-of-range value (zero, negative, not a
  number) be rejected at startup, that the defaults be documented where the
  project documents its variables, or that the effective values be logged
  at startup, all pass.
  FAIL if REQUIREMENTS makes either tunable required, removes its default,
  or has the job refuse to start when the variable is absent.
weight: 2
---

Leaves a production-safe default in place: the fail-fast rule is for a
value whose default would be wrong in production, not for every new
variable.

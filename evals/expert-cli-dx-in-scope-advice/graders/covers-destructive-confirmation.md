---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  specific brief, that `prune-logs` deletes files (a destructive, irreversible
  operation run unattended from cron) and therefore needs a `--dry-run` mode
  and/or a `--force`/confirmation safeguard against an over-broad `--older-than`
  value or wrong directory wiping out logs that were still needed.
  FAIL if the reply never raises the destructive-deletion risk, or only
  restates a generic "be careful with destructive commands" checklist without
  connecting it to this brief's cron/unattended-deletion scenario.
weight: 2
---

Names the destructive-deletion / dry-run / confirmation concern, tailored to
the unattended `prune-logs` scenario.

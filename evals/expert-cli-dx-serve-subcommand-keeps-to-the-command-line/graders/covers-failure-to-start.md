---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS or TEST SCENARIOS names, tailored to this
  brief, how `agentd serve` behaves when it cannot start — the port already
  taken, or the `--config` file missing or unreadable — with a non-zero exit
  code and an actionable message on stderr (what failed and what to do),
  so the entrypoint's failure is visible to the orchestrator instead of the
  command idling or exiting 0.
  FAIL if the reply never addresses what the command does when the port is
  taken or the config file is missing, or lets such a failure exit 0 or
  print only to stdout.
weight: 2
---

Names the command's failure to start — port taken, config missing — with
a non-zero exit and an actionable message, tailored to the entrypoint
scenario.

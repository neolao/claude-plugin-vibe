---
type: llm
focus: last_message
criteria: |
  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, tailored to this
  specific brief, that the long-running daemon must handle SIGTERM/SIGINT
  (from the supervisor stopping/restarting it or the machine shutting down),
  terminate its spawned per-file child processes, and leave no orphaned
  processes behind.
  FAIL if the reply never raises signal handling / child-process cleanup for
  this daemon's shutdown/restart scenario.
weight: 2
---

Names SIGTERM/SIGINT handling and child-process cleanup for the daemon's
shutdown/restart scenario.

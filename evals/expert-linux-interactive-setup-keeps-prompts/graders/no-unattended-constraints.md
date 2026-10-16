---
type: llm
focus: last_message
criteria: |
  Nothing schedules this script: a developer launches it from their own
  terminal, one laptop each, so a single-instance guard and a scheduler's
  bare environment are concerns of another kind of script. The request also
  asks for task-specific entries only, no generic checklist.

  PASS if no REQUIREMENTS, RISKS, or TEST SCENARIOS entry requires a lock or
  single-instance guard (`flock`, a lock file, "two runs must not overlap"),
  nor frames a requirement or a test around cron, a systemd timer or a
  supervisor launching the script. Requiring that a rerun after a pull is
  safe (idempotent installs, the config file not clobbered) is a different
  concern and passes.
  FAIL if the reply requires a lock or single-instance guard, or writes a
  requirement or a test scenario in which cron, a timer or a supervisor runs
  the script.
weight: 2
---

Does not impose a lock or scheduler-run constraints on a script a developer
runs by hand.

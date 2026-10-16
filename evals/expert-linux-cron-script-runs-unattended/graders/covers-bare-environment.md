---
type: llm
focus: last_message
criteria: |
  The script worked from the engineer's terminal and now runs from cron,
  whose environment is not the interactive shell's: `/opt/pgsql/bin` and
  `/usr/local/bin` are not on cron's default `PATH`.

  PASS if REQUIREMENTS, RISKS, or TEST SCENARIOS names, for this script,
  that the cron run does not inherit the engineer's shell environment and
  that `PATH` must be set explicitly in the script (or in the crontab), or
  the tools called by absolute path, so `psql` and `csvcheck` resolve under
  cron.
  FAIL if the reply never raises the difference between the engineer's
  terminal environment and cron's for locating `psql` and `csvcheck`.
weight: 2
---

Names the bare cron environment and requires an explicit `PATH` (or absolute
paths) for the tools under `/opt/pgsql/bin` and `/usr/local/bin`.

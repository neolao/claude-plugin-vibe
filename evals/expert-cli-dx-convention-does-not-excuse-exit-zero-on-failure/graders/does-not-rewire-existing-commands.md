---
type: llm
focus: last_message
criteria: |
  The ops team's wrapper scripts run the six existing commands under
  `set -e` and read their `ERROR:` line on stdout: making those commands
  exit non-zero or move their errors to stderr would abort or blind every
  one of those scripts, and the brief adds one command; nothing else
  changes.

  PASS if no REQUIREMENTS entry makes changing the six existing commands'
  exit codes or error output a non-negotiable of this change. The gap may
  be named in RISKS, as a later migration, or as advice for a future change:
  that passes.
  FAIL if REQUIREMENTS demands that the existing commands exit non-zero,
  move their `ERROR:` line to stderr, or be changed as part of this change.
weight: 1
---

Keeps the six existing commands out of this change's REQUIREMENTS:
consistency is restored by a named follow-up, not by breaking the wrapper
scripts now.

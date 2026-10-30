---
type: llm
focus: last_message
criteria: |
  The brief says a developer runs this script by hand from a terminal and
  that it asks them which services to install. Those questions are the
  script's purpose, not a defect: the rule that a prompt must not hang
  applies to scripts launched by cron, a timer or a supervisor, which this
  one never is.

  PASS if no REQUIREMENTS, RISKS, or TEST SCENARIOS entry forbids the script
  from asking the developer its questions in the terminal, or turns the
  script into one that must run without a terminal. Requiring that the
  answers be validated, that a default be offered, that the chosen services
  be confirmable from flags *in addition to* the questions, that the script
  exit with a message when no terminal is attached, or that the package
  manager be called with its own yes flag (`-y`, `--noconfirm`) once the
  developer has already chosen what to install, is fine: none of that removes
  the script's questions.
  FAIL if the reply requires the script to run without prompting the
  developer, treats the questions to the developer as a risk to remove, or
  frames the script as unattended (cron, CI, a supervisor) and demands the
  non-interactive hardening that goes with it.
weight: 2
---

Does not strip an interactive setup script of its questions by applying the
unattended-run rule to a script run by hand.

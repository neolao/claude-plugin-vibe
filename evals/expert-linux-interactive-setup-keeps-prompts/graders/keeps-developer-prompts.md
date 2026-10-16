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
  from asking the developer its questions in the terminal, or requires every
  call to be made non-interactive. Requiring that the answers be validated,
  that a default be offered, that the chosen services be confirmable from
  flags *in addition to* the questions, or that the script exit with a
  message when no terminal is attached, is fine: none of that removes the
  questions.
  FAIL if the reply requires the script to run without prompting, treats the
  questions to the developer as a risk to remove, or requires the package
  manager's own interactive prompts to be suppressed on the grounds that the
  script runs unattended.
weight: 2
---

Does not strip an interactive setup script of its questions by applying the
unattended-run rule to a script run by hand.

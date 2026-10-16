---
type: llm
focus: last_message
criteria: |
  A confirmation prompt, per-step progress and a failure message are flows
  and feedback, but the brief changes a terminal command only: there is no
  screen, and the command's prompts, output and exit status are the
  domain of the CLI expert, whose checklist carries the CLI-specific form
  of those rules (a prompt on a non-TTY fails naming the flag instead of
  hanging the unattended CI run). The expert's own scope sentence hands a
  command-line interface to that expert even though a command has steps
  and feedback too, with a one-line reply whatever format the request asks
  for.

  PASS if the sub-agent's reply is a short statement (roughly one line, or
  a short reply that explicitly says this is a command-line interface and
  hands it to another expert) and it does NOT produce REQUIREMENTS/RISKS/
  TEST SCENARIOS about the confirmation prompt, the progress output, the
  failure message, the summary, or what happens when the command runs in
  CI.
  FAIL if the reply fills the three lists, or asserts confident detailed
  advice about the prompt, the output, the error wording or the unattended
  run, as if the brief were in scope — even advice that would be right for
  a graphical interface.
weight: 2
---

Declines the terminal-only brief in one line instead of prescribing the
command's prompts, output and failure behavior.

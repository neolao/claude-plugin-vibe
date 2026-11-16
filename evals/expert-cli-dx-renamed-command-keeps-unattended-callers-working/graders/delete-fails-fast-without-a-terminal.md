---
type: llm
focus: last_message
criteria: |
  `vault delete` is new and asks for confirmation. The expert's checklist
  says a prompt on a non-TTY fails naming the flag instead of hanging.

  PASS if REQUIREMENTS or TEST SCENARIOS says that `vault delete <name>`
  run with no terminal and without the skip flag (whatever it is called:
  `--yes`, `--force`…) deletes nothing, does not wait for input, and exits
  non-zero with a message naming that flag; and that the flag deletes
  without asking.
  FAIL if the reply lets `vault delete` wait for an answer on a non-TTY,
  makes it delete silently there without the flag, or never defines how
  `vault delete` behaves with no terminal attached.
weight: 1
---

Defines the new command's unattended behaviour: fail fast and name the skip
flag, never hang and never delete unasked.

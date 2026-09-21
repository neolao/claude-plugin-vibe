---
type: llm
focus: last_message
criteria: |
  `subprocess.run` is called with an argument list and `shell=False`, so no
  shell parses the input.

  PASS if no `high` or `medium` severity Injection finding claims command or
  shell injection here.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call a list-form, shell-less subprocess call shell injection.

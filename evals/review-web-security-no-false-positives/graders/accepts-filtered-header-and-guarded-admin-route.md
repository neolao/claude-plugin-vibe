---
type: llm
focus: last_message
criteria: |
  `set_nickname` strips everything outside a safe character set before
  writing the `X-Nickname` header, and `delete_user` sits behind a
  `require_admin` decorator that checks an admin token first.

  PASS if no `high` or `medium` severity Header injection or Access control
  finding targets either.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not flag a character-filtered header write or an auth-guarded admin route.

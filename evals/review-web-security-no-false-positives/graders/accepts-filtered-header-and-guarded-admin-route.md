---
type: llm
focus: last_message
criteria: |
  `set_nickname` strips everything outside a safe character set before
  writing the `X-Nickname` header, and `delete_user` sits behind a
  `require_admin` decorator that compares the supplied token, in constant
  time, to an `ADMIN_TOKEN` read at startup with `os.environ[...]` (the app
  does not start without it, and a missing header compares as `""`).

  PASS if no `high` or `medium` severity Header injection, Access control,
  or Auth bypass finding targets either. A report
  with no findings at all passes, and so does one that does not mention them.
  FAIL only if either is flagged at high or medium severity.
weight: 1
---

Does not flag a character-filtered header write or an auth-guarded admin route.

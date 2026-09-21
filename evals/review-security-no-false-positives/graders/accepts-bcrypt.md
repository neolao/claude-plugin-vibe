---
type: llm
focus: last_message
criteria: |
  Passwords are hashed with `bcrypt`, a current password-hashing function.

  PASS if no `high` or `medium` severity Crypto finding calls this weak,
  outdated, or broken.
  FAIL if it is flagged at high or medium severity.
weight: 1
---

Does not call bcrypt weak crypto.

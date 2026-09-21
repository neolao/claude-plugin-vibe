---
type: llm
focus: last_message
criteria: |
  `API_KEY` is read from `os.environ`, and `.env.example` holds only
  placeholder values — no real credential is committed.

  PASS if no `high` or `medium` severity Secret finding claims a hardcoded
  credential or a committed secret here.
  FAIL if either the env lookup or the placeholder file is flagged at high
  or medium severity.
weight: 1
---

Does not call an env-sourced key or a placeholder `.env.example` a committed secret.

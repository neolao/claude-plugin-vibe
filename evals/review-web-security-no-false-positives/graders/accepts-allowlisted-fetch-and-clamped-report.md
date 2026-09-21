---
type: llm
focus: last_message
criteria: |
  `fetch_avatar` checks the target hostname against `ALLOWED_AVATAR_HOSTS`
  before fetching, and `report` clamps `rows` to a fixed maximum whatever
  the client sends.

  PASS if no `high` or `medium` severity SSRF or DoS finding targets either.
  FAIL if either is flagged at high or medium severity.
weight: 1
---

Does not flag an allowlisted fetch or a clamped row count.

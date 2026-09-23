---
type: llm
focus: last_message
criteria: |
  `fetch_avatar` accepts only `https` URLs whose hostname is in
  `ALLOWED_AVATAR_HOSTS`, and fetches through an opener that refuses
  redirects, with a timeout. `report` parses `rows` as an integer and clamps
  it between 1 and a fixed maximum whatever the client sends.

  PASS if no `high` or `medium` severity SSRF or DoS finding targets either. A report
  with no findings at all passes, and so does one that does not mention them.
  FAIL only if either is flagged at high or medium severity.
weight: 1
---

Does not flag an allowlisted fetch or a clamped row count.

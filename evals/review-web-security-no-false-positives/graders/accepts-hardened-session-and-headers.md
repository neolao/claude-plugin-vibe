---
type: llm
focus: last_message
criteria: |
  `login` sets `session_id` with `httponly=True, secure=True,
  samesite="Strict"`, `whoami` returns a generic message and logs the real
  exception server-side, and `add_security_headers` sets CSP,
  X-Content-Type-Options, X-Frame-Options and HSTS on every response.

  PASS if no `high` or `medium` severity Cookies, Info disclosure, or
  Security headers finding targets any of the three.
  FAIL if any is flagged at high or medium severity.
weight: 1
---

Does not flag a hardened cookie, a generic error body, or headers that are present.

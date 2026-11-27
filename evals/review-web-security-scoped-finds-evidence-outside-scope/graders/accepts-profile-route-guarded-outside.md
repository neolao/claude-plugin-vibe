---
type: llm
focus: last_message
criteria: |
  `profile` in fixtures/portal/routes/account.py renders the signed-in
  visitor's own profile from `session["user_id"]`; `require_login` in
  fixtures/portal/app.py, outside the scope, aborts every `/account/`
  request with no session, so the route only answers signed-in visitors
  about themselves.

  PASS if no `high` or `medium` severity finding reports `profile` as
  missing authentication or access control. A report that does not
  mention it passes.
  FAIL if `profile` is reported as unauthenticated, or as reachable by
  another user, at high or medium severity.
weight: 1
---

Does not call a route unauthenticated when a hook outside the scope
guards it.

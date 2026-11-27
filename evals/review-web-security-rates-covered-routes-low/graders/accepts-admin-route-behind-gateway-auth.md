---
type: llm
focus: last_message
criteria: |
  `delete_user` in fixtures/app.py has no decorator and no session check
  of its own; fixtures/deploy/nginx.conf, the only way into the app per
  fixtures/deploy/docker-compose.yml, sends every `/admin/` request
  through `auth_request /oauth2/auth` (an oauth2-proxy restricted to the
  `support` group) before proxying it, so the route only answers support
  staff.

  PASS if no `high` or `medium` severity `Access control` (or clearly
  equivalent category name) finding targets `delete_user`. A `low`
  finding passes, and so does a report with no findings at all.
  FAIL if `delete_user` is reported as unauthenticated or reachable by
  anyone at high or medium severity.
weight: 2
---

Counts a gateway rule a file of the repository applies as the route's
guard.

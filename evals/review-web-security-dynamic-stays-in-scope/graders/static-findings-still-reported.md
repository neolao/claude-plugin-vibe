---
type: llm
focus: last_message
criteria: |
  Dynamic mode is additional to the static review, not a replacement for it.

  PASS if the report still contains at least three distinct static findings on
  `fixtures/app.py` — for example the `send_file` path built from
  `<path:filename>`, the search term interpolated into HTML, the unauthenticated
  `/admin/users/<user_id>/delete` route, the user-supplied URL fetched in
  `/fetch-avatar`, or the exception text returned by `/whoami`.
  FAIL if enabling dynamic verification collapses the report to a note about
  the dynamic pass with fewer than three static findings.
weight: 2
---

Keeps the static pass when dynamic verification is enabled.

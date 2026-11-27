---
type: llm
focus: last_message
criteria: |
  `delete_user` in fixtures/app.py removes an account on a POST with no
  decorator, no session check and nothing in front of it:
  deploy/nginx.conf proxies every path to the app with no
  authentication, so anyone on the Internet triggers it with a plain
  request.

  PASS if the reported findings include an `Access control` (or clearly
  equivalent category name) finding on `delete_user` with `SEVERITY:
  high`.
  FAIL if no finding reports `delete_user`, or if it is rated `medium` or
  `low`.
weight: 2
---

Rates a route anyone reaching it triggers with what it already accepts
high.

---
type: llm
focus: last_message
criteria: |
  `add_headers` in fixtures/portal/app.py, outside the scope, sets
  Content-Security-Policy, X-Content-Type-Options, X-Frame-Options,
  Referrer-Policy, Strict-Transport-Security and Permissions-Policy on
  every response; no route under fixtures/portal/routes/ sets or removes
  a header.

  PASS if no `Security headers` (or clearly equivalent category name)
  finding is reported, on any route or on the hook. A report that does
  not mention headers passes.
  FAIL if any finding reports missing or weak security headers, on a route
  in scope or on fixtures/portal/app.py.
weight: 1
---

Reports a response-wide property once, on the hook that sets it, and not
at all when that hook is outside the scope and complete.

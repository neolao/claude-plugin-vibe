---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Security headers` (or clearly
  equivalent category name) finding on the `add_headers` `after_request`
  hook in fixtures/app.py, for existing but never actually setting any
  security header (no CSP, X-Content-Type-Options, X-Frame-Options,
  Strict-Transport-Security, etc.) on any response.
  FAIL if no finding flags the missing security headers across the app.
weight: 1
---

Reports the app's missing Content-Security-Policy/X-Content-Type-Options/
X-Frame-Options/HSTS headers as a `Security headers` finding.

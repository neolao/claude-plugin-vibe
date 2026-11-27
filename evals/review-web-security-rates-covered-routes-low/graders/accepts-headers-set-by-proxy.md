---
type: llm
focus: last_message
criteria: |
  fixtures/app.py sets no security header; fixtures/deploy/nginx.conf,
  the proxy every response passes through, adds Content-Security-Policy,
  X-Content-Type-Options, X-Frame-Options, Referrer-Policy,
  Strict-Transport-Security and Permissions-Policy on every response.

  PASS if no `high` or `medium` severity `Security headers` (or clearly
  equivalent category name) finding is reported. A `low` finding passes,
  and so does a report with no findings at all.
  FAIL if any finding reports the headers as missing at high or medium
  severity.
weight: 2
---

Counts a header the proxy config in the repository adds as applied.

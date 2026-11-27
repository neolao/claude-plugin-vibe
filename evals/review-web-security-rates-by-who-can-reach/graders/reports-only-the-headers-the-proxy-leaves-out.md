---
type: llm
focus: last_message
criteria: |
  fixtures/app.py sets no security header; fixtures/deploy/nginx.conf, the
  proxy every response passes through, adds `X-Frame-Options` and
  `Strict-Transport-Security` on every response and nothing else, so the
  responses lack `Content-Security-Policy` and `X-Content-Type-Options`
  (and `Referrer-Policy`, `Permissions-Policy`), but not the two the
  proxy adds.

  PASS if the reported findings include a `Security headers` (or clearly
  equivalent category name) finding that names `Content-Security-Policy`
  or `X-Content-Type-Options` as missing, and no finding names
  `X-Frame-Options` or `Strict-Transport-Security` as missing or absent.
  A finding that mentions the two as already set by nginx passes.
  FAIL if no finding reports the missing headers, or if any finding
  lists `X-Frame-Options` or `Strict-Transport-Security` among the
  missing ones.
weight: 2
---

Counts a header the proxy config in the repository adds as applied, and
reports only the ones nothing sets.

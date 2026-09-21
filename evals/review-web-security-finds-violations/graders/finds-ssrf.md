---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `SSRF` (or clearly equivalent
  category name) finding on `fetch_avatar` in fixtures/app.py, for fetching
  a URL taken directly from the `url` query parameter with no allowlist,
  letting an attacker reach internal hosts or a cloud metadata endpoint.
  FAIL if no finding flags `fetch_avatar`'s unrestricted URL fetch.
weight: 1
---

Reports `fetch_avatar`'s unrestricted attacker-controlled URL fetch as an
`SSRF` finding.

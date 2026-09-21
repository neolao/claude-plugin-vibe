---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include an `XSS` (or clearly equivalent
  category name) finding on `search` in fixtures/app.py, for embedding the
  unescaped `q` query parameter directly into the returned HTML.
  FAIL if no finding flags `search`'s unescaped HTML interpolation.
weight: 1
---

Reports `search`'s unescaped reflection of `q` into HTML as an `XSS`
finding.

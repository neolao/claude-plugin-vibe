---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Header injection` (or clearly
  equivalent category name) finding on `set_nickname` in fixtures/app.py,
  for writing the unsanitized `nickname` query parameter directly into the
  `X-Nickname` response header, allowing CR/LF injection.
  FAIL if no finding flags `set_nickname`'s unsanitized header write.
weight: 1
---

Reports `set_nickname`'s unsanitized `X-Nickname` header write as a
`Header injection` finding.

---
type: llm
focus: last_message
criteria: |
  "On an empty file it returns an empty list": fixtures/parser.py:9-10
  raises `ValueError` on an empty file.

  PASS if a `(contradicted)` finding quotes that claim and says the cited
  lines raise (ValueError) instead of returning an empty list, with a fix.
  FAIL if the claim is accepted, or flagged only as unproven without reading
  the cited lines.
weight: 2
---

The source says the opposite of the text: contradicted, with the source
quoted.

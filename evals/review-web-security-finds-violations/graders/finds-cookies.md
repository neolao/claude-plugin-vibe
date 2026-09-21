---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Cookies` (or clearly equivalent
  category name) finding on `login` in fixtures/app.py, for setting the
  `session_id` cookie without `HttpOnly`, `Secure`, or `SameSite`.
  FAIL if no finding flags the `session_id` cookie's missing attributes.
weight: 1
---

Reports `login`'s `session_id` cookie missing HttpOnly/Secure/SameSite as
a `Cookies` finding.

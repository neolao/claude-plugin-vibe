---
type: llm
focus: last_message
criteria: |
  `.env.example` holds `sk_test_your_key_here`, `whsec_your_secret_here`
  and `changeme`: samples in an example file, shaped like nothing a
  provider issues.

  PASS if no finding reports `.env.example` or any of its values as a
  committed secret. A report with no findings at all passes.
  FAIL if a `Secret` (or clearly equivalent category name) finding targets
  `.env.example`.
weight: 1
---

Does not call the samples of `.env.example` committed secrets.

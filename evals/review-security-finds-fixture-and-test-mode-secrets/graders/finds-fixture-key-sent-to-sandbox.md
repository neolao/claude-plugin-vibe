---
type: llm
focus: last_message
criteria: |
  `tests/fixtures/postal_account.yaml` holds a well-formed Postal API key
  (`api_key: pk_…`); `tests/test_mail.py` reads it and `mail.send` puts it
  in the `X-Postal-Key` header of a request to `https://api.postal.example`,
  the provider's host — the README says the tests run against the
  sandbox account. Nothing in the repository labels the value as fake, and
  no stub receives it: it authenticates to the provider.

  PASS if the reported findings include a `Secret` (or clearly equivalent
  category name) finding, at any severity, whose FILE: line points to
  tests/fixtures/postal_account.yaml or tests/test_mail.py and that names
  this key as a committed credential.
  FAIL if no finding reports the key, or if it is dismissed as a test
  fixture or a placeholder.
weight: 2
---

Reports a well-formed key in a test fixture when the test sends it to the
provider rather than to a stub.

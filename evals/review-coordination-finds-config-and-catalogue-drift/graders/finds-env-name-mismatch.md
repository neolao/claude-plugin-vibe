---
type: llm
focus: last_message
criteria: |
  fixtures/app/settings.py reads `PAYMENT_TIMEOUT_SECONDS` from the
  environment with no default, while fixtures/deploy/app.env sets
  `PAYMENT_TIMEOUT_SEC`: the two names already differ, so the service
  fails at start-up with a KeyError.

  PASS if the reported findings include one anchored on
  fixtures/app/settings.py that names both variable spellings
  (`PAYMENT_TIMEOUT_SECONDS` and `PAYMENT_TIMEOUT_SEC`) and says they
  already differ (a start-up failure, a KeyError or a missing variable).
  FAIL if no finding names both spellings, or if it presents them as
  agreeing.
weight: 2
---

Finds a configuration name written in the code and in the deploy manifest.

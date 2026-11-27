---
type: llm
focus: last_message
criteria: |
  `STUB_API_KEY` in tests/conftest.py is a well-formed Postal key that the
  suite hands only to `PostalStub`, the HTTP server the same file starts
  on 127.0.0.1; `test_mail.py` sends it to that server's URL, and
  `notifier/mail.py` reads the real key from `POSTAL_API_KEY` in the
  environment. The value authenticates to nothing outside the test run.

  PASS if no `high` or `medium` severity `Secret` (or clearly equivalent
  category name) finding targets `STUB_API_KEY`, tests/conftest.py or the
  key as sent by test_mail.py. A `low` finding passes, and so does a
  report with no findings at all.
  FAIL if the stub key is reported as a committed credential at high or
  medium severity.
weight: 2
---

Does not call a well-formed value a committed secret when the suite hands
it only to a stub it starts itself.

---
type: llm
focus: last_message
criteria: |
  fixtures/cli/main.py reads `APP_ENV` as a string and passes it on
  unparsed; fixtures/cli/export.py, fixtures/cli/storage.py and
  fixtures/cli/alerts.py each compare it to `"production"` / `"staging"`
  literals (storage.py even spells `"stagng"`).

  PASS if the reported findings include a `Stringly-typed code` (or
  clearly equivalent category name) finding on the environment string
  comparisons in at least one of export.py, storage.py or alerts.py,
  proposing an enum or constants parsed once at the boundary.
  FAIL if no finding flags these downstream string comparisons, or if the
  only finding is on the `os.environ.get` read itself.
weight: 2
---

Reports the downstream comparisons as Stringly-typed: the boundary read is
fine, the string carried past it and compared in three places is the
pattern.

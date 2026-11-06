---
type: llm
focus: last_message
criteria: |
  `_strip_currency` in fixtures/pricing/amounts.py is private (leading
  underscore), exempt from the fixture's docstring rule, and its docstring
  `"""Strip the currency symbol from the text."""` only restates its name.

  PASS if the reported findings include a `Redundant` (or clearly
  equivalent category name) finding on that docstring whose SUGGESTION is
  to delete it.
  FAIL if no finding flags the `_strip_currency` docstring, or if the
  finding keeps it.
weight: 1
---

Still deletes the redundant docstring the convention does not require: the
exemption is for what the convention covers, not for every docstring in a
repo that has a convention.

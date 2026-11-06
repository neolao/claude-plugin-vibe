---
type: llm
focus: last_message
criteria: |
  `_fmt(d)` and `_label(s)` in fixtures/api/presenters.py are presentation
  helpers with one-letter parameters; the business words of the file
  (`Subscription`, `plan`, `status`, `period_end`) are the ones the rest of
  the code uses.

  PASS if no `high` or `medium` severity Ubiquitous language (or any other)
  finding targets `_fmt`, `_label`, `d` or `s` for being terse, vague or
  abbreviated. A report with no findings at all passes.
  FAIL if one of those names is flagged at high or medium severity.
weight: 1
---

Does not judge name clarity: that is review-naming's question, not whether
a word is the business's.

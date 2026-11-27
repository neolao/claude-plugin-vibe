---
type: llm
focus: last_message
criteria: |
  `default_locale` in fixtures/settings.py is a pure function under
  `functools.lru_cache(maxsize=8)`, called once by `load_settings` when
  the settings file has no locale line, itself called once by `start` in
  fixtures/app.py.

  PASS if no `high` or `medium` severity Premature optimization (or
  equivalent) finding targets `default_locale` or its `lru_cache`. A
  `low` finding passes, as does a report with no findings at all.
  FAIL if the memoization is flagged at high or medium severity.
weight: 1
---

A memoized pure function on a cold path is contained machinery: `low`
at most.

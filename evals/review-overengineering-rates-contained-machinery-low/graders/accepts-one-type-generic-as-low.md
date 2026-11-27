---
type: llm
focus: last_message
criteria: |
  `Box(Generic[T])` in fixtures/settings.py is instantiated with one
  type, `Settings`, by `load_settings`, and read by `start` in
  fixtures/app.py through `box.value`.

  PASS if no `high` or `medium` severity Speculative abstraction or
  Pattern without need (or equivalent) finding targets `Box`, `T` or the
  `Box[Settings]` return type. A `low` finding passes, as does a report
  with no findings at all.
  FAIL if `Box` is flagged at high or medium severity.
weight: 1
---

A generic with one type argument is contained machinery: `low` at most.

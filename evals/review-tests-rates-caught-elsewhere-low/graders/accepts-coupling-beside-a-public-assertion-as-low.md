---
type: llm
focus: last_message
criteria: |
  `test_compute_returns_the_function_result` in fixtures/test_memo.py
  asserts `memo.compute(4) == 16` — the public result — and then
  `assertIn(4, memo._cache)`, a private detail; the next test,
  `test_compute_calls_the_function_once_per_input`, pins the caching
  through the public call count. A wrong `compute` fails the first
  assertion, a cache that stops caching fails the second test: the
  `_cache` peek costs upkeep on a refactor and nothing else.

  PASS if no `high` or `medium` severity `Implementation-coupled` (or
  clearly equivalent category name) finding targets the `_cache`
  assertion. A `low` finding passes, and so does a report with no
  findings at all.
  FAIL if the `_cache` assertion is reported at high or medium severity.
weight: 2
---

Coupling on a private detail beside a public assertion that already pins
the result is poor upkeep, not a regression that ships: low at most.

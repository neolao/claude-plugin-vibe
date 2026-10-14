---
type: llm
focus: last_message
criteria: |
  `retry` in fixtures/client.py takes `attempts` and `delay`; its callers
  pass `attempts=1`, `attempts=5, delay=2`, and rely on the defaults.

  PASS if no finding reports `attempts` or `delay` as an `Unused generality`
  (parameter receiving one value everywhere, or unexercised option).
  FAIL if `Unused generality` is reported on `retry`'s parameters.
weight: 1
---

Does not flag parameters that callers actually vary.

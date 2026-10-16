---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Timeout/limit` (or clearly
  equivalent category name) finding on the carrier rate lookup in
  `dispatch_parcel` (fixtures/shipping/dispatch.py): it calls `get_json`
  without a `timeout`, and `get_json` (fixtures/carriers/http.py) defaults
  `timeout` to `None`, so `requests` waits forever on a carrier that stops
  answering and the scanner thread hangs with it. The finding may name the
  missing argument, the `None` default, or both.
  FAIL if no finding flags this rate lookup as having no timeout.
weight: 1
---

Reports the `get_json` call in `dispatch_parcel` as having no timeout.
dispatch.py alone shows a helper call; only carriers/http.py, outside the
scope, shows the default is `None`.

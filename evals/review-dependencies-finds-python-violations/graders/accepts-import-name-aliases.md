---
type: llm
focus: last_message
criteria: |
  Three packages are imported under a name that differs from their
  distribution name: `beautifulsoup4` as `bs4` and `python-dateutil` as
  `dateutil` in fixtures/src/report_builder/render.py, `pycrypto` as
  `Crypto` in fixtures/src/report_builder/signing.py. All three are used
  by runtime code.
  PASS if no `Unused` or `Misplaced` finding, at any severity, targets
  `beautifulsoup4`, `python-dateutil` or `pycrypto`.
  FAIL if any of them is called unused or misplaced.
weight: 1
---

Does not call a package unused because its import name differs from its
distribution name.

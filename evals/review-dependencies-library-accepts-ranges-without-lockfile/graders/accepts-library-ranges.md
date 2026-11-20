---
type: llm
focus: last_message
criteria: |
  fixtures/pyproject.toml declares a library published to PyPI
  (fixtures/README.md installs it with `pip install slugkit`, the manifest
  has a PyPI homepage and no entry point). Its runtime dependencies are
  declared as lower-bounded ranges: `unidecode>=1.3` and
  `python-dateutil>=2.8`. A library declares ranges so that the
  applications installing it can resolve their own versions: the ranges
  are the convention, not a defect.

  PASS if no `high` or `medium` severity `Version hygiene` finding targets
  `unidecode` or `python-dateutil` for its `>=` range. Only a finding block
  (`PACKAGE:` ... `CATEGORY:` ... `SEVERITY:`) counts; a sentence of prose
  mentioning the ranges is not a finding. A report whose only finding says
  the audit tool could not run passes.
  FAIL if either range is flagged as `Version hygiene` at high or medium
  severity.
weight: 1
---

Does not flag a library's lower-bounded ranges as floating versions.

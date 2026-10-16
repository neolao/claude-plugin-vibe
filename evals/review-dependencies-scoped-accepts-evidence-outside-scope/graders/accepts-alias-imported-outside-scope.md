---
type: llm
focus: last_message
criteria: |
  `python-dateutil` is declared in `[project] dependencies` of
  fixtures/pyproject.toml and imported under the name `dateutil`
  (`from dateutil.relativedelta import relativedelta`) by
  fixtures/reports/aging.py, outside the scope (fixtures/orders/).

  PASS if no `Unused` or `Misplaced` finding, at any severity, targets
  `python-dateutil`. A report whose only finding says the audit tool could
  not run passes.
  FAIL if `python-dateutil` is called unused or misplaced.
weight: 1
---

Does not call a package unused when its import name differs from its
distribution name and its only importer sits outside the path under review.

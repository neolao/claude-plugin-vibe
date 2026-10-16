---
type: llm
focus: last_message
criteria: |
  fixtures/billing/__init__.py imports `export_invoices_csv` and
  `InvoiceNumberSequence` without using them in that file: it re-exports
  them, lists both in `__all__`, and fixtures/cli/main.py and
  fixtures/workers/nightly.py import them from the `billing` package.

  PASS if no `high` or `medium` severity finding calls either import in
  fixtures/billing/__init__.py unused, a leftover or dead code. A report
  with no findings at all passes.
  FAIL if either re-export is flagged at high or medium severity as an
  unused import (or equivalent).
weight: 1
---

Does not call a package `__init__` re-export an unused import: the name is
used by the modules that import it from the package.

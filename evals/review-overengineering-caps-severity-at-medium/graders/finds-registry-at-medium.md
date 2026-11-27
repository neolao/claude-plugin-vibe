---
type: llm
focus: last_message
criteria: |
  fixtures/src/plugins/registry.py keeps a `_PLUGINS` dict fed by a
  `register` decorator and read by `load`; the only registration is
  `CsvImport` in fixtures/src/plugins/csv_import.py, and the only
  consumer, fixtures/src/plugins/run_import.py, imports that module for
  its side effect and then calls `load("csv")`.

  PASS if the reported findings include a `Speculative abstraction` or
  `Pattern without need` (or clearly equivalent category name) finding
  on the registry (`_PLUGINS`, `register`, `load` or
  fixtures/src/plugins/registry.py) with SEVERITY `medium`.
  FAIL if no finding reports the registry as machinery one plugin does
  not need, or if that finding carries SEVERITY `high` or `low`.
weight: 2
---

Reports the one-plugin registry at `medium`: the registry must be fed
by a side-effect import for anything to happen, a cost every reader
pays today.

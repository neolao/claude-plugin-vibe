---
type: llm
focus: last_message
criteria: |
  `ExportSettings(chunk_size, delimiter)` in fixtures/export_settings.py
  is built with `chunk_size=500, delimiter=";"` in
  fixtures/accounting_export.py and `chunk_size=5000, delimiter=","` in
  fixtures/inventory_export.py; `CsvExporter.write` reads both fields.

  PASS if no `high` or `medium` severity finding (Unused configurability,
  Pattern without need, Speculative abstraction or any other category)
  targets `ExportSettings`, `chunk_size`, `delimiter` or `CsvExporter`.
  A `low` finding passes, and so does a report with no findings at all.
  FAIL if one of them is reported at high or medium severity — for
  holding the same value everywhere, or as a wrapper that adds nothing.
weight: 2
---

Does not call a settings object unused configurability when its two
call sites set different values that the consumer reads.

---
type: llm
focus: last_message
criteria: |
  `ExportSettings(chunk_size, delimiter)` in fixtures/export_settings.py
  is built at two call sites, fixtures/accounting_export.py and
  fixtures/inventory_export.py, both with `chunk_size=500, delimiter=","`;
  `CsvExporter` in fixtures/csv_exporter.py stores it at construction and
  reads both fields later in `write`.

  PASS if the reported findings include an `Unused configurability` (or
  clearly equivalent category name) finding whose FILE: line points to
  fixtures/export_settings.py, fixtures/csv_exporter.py or one of the two
  call sites, that names `ExportSettings`, `chunk_size` or `delimiter`,
  and whose ISSUE or SUGGESTION says the two call sites set the same
  values (or that nothing varies them).
  FAIL if no finding reports the settings for always holding the same
  values.
weight: 2
---

Reports a knob a component carries — taken at construction, read
later — that every call site sets to the same literal.

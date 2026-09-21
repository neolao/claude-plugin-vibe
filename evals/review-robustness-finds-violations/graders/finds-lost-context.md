---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Lost context` (or clearly
  equivalent category name) finding on `load_export_template` in
  fixtures/export_writer.py, for catching `Exception as e` and re-raising a
  brand-new `Exception("failed to load template")` that drops the original
  cause (no `raise ... from e`) and omits the `path` that failed, so a
  caller can't tell which template or why.
  FAIL if no finding flags this rethrow for losing the original cause or the
  missing identifier.
weight: 1
---

Reports the cause-dropping, identifier-less rethrow in
`load_export_template` as a `Lost context` finding.

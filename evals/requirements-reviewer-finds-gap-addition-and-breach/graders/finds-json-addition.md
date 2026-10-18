---
type: llm
focus: last_message
criteria: |
  The request asks for a CSV only. `to_json` and the `fmt == "json"` branch
  of `export_report` add a JSON export nobody asked for.

  PASS if an `(addition)` finding points at `to_json` and/or the json branch
  (fixtures/export.py, lines 17-18 or 22-24) and says no requirement covers
  a JSON export, with a fix (remove it).
  FAIL if the JSON export is not reported as an addition.
weight: 2
---

A visible behaviour the request never asked for is an addition.

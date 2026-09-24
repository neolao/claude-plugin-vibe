---
type: llm
focus: last_message
criteria: |
  FAIL if any finding flags the `open(...)` + `csv.DictReader` read of
  `postcode_zones.csv` at the top of fixtures/shipping/zones.py as blocking
  I/O or per-request work. That read runs once, when the module is imported
  at startup, not on a request path.
  A `Complexity` finding on `zone_for`'s lookup over the loaded list does not
  count against this grader, even if it suggests building a dict at load
  time, and neither does a report that mentions the load only to say it is
  fine.
  PASS otherwise, including when the report has no finding at all.
weight: 1
---

Does not flag the import-time CSV load in zones.py as blocking I/O.

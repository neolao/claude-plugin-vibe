---
type: llm
focus: last_message
criteria: |
  `record_heartbeat` in fixtures/telemetry/devices.py writes the
  module-level `_last_seen` dict, keyed by device id, on every heartbeat
  (`heartbeat` in fixtures/telemetry/app.py, one per sensor every 30
  seconds); nothing evicts, caps or expires its entries, so the dict keeps
  one entry per sensor ever seen while the README says the fleet of a few
  hundred thousand sensors is replaced every couple of years.

  PASS if the reported findings include an `Unbounded` (or clearly
  equivalent category name) finding on `_last_seen` or `record_heartbeat`
  in fixtures/telemetry/devices.py, saying it grows with the sensors ever
  seen (or has no eviction, cap or expiry) for the life of the process.
  FAIL if no finding reports `_last_seen` as growing without bound.
weight: 2
---

Reports the map that legitimate traffic grows, one entry per device ever
seen, as Unbounded.

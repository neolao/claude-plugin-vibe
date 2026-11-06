# Module: metrics

**Role:** In-process counters of placed orders and their totals, to be read by
the health endpoint.
**Files:** `metrics/collector.py`
**Exports:** `Collector.record(total_cents)`, `Collector.snapshot() -> dict`
**Depends on:** (none)

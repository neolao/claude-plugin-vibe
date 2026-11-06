---
type: llm
focus: last_message
criteria: |
  The scope is fixtures/core/events.py and fixtures/metrics/collector.py.
  fixtures/core/events.py imports `adapters.audit_log` (outside the
  scope), while fixtures/adapters/postgres_gateway.py and
  fixtures/adapters/smtp_notifier.py import `core.ports` and
  `.vibe/modules/adapters.md` declares `adapters` depends on `core`: the
  in-scope import closes a core/adapters cycle and points outward from the
  innermost layer.

  PASS if the reported findings include a `Circular dependency` or a
  `Layer direction` (or clearly equivalent category name) finding anchored
  on fixtures/core/events.py whose ISSUE or SUGGESTION names
  fixtures/adapters/audit_log.py (or `AuditLog`) as the other end.
  FAIL if no finding flags the `adapters.audit_log` import of
  fixtures/core/events.py, or if the finding names no file outside the
  scope as the other end.
weight: 2
---

Reports the cycle whose in-scope edge is the changed file, naming the
outside end as evidence.

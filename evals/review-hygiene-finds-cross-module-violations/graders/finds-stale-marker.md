---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Stale marker` (or clearly
  equivalent category name) finding on the `# FIXME: the refund is a cent
  short on some orders` comment in fixtures/billing/refunds.py, for a marker
  with no backlog item or issue reference.
  FAIL if no finding flags this FIXME as a stale marker.
weight: 1
---

Reports the ticket-less `FIXME` in fixtures/billing/refunds.py as a `Stale
marker` finding.

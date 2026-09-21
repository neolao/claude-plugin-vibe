---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Stale marker` (or clearly
  equivalent category name) finding on the `# TODO: handle the case where
  store is empty` comment in fixtures/cache_refresh.py, for a TODO with no
  backlog item or issue reference attached.
  FAIL if no finding flags this TODO as a stale marker.
weight: 1
---

Reports the ticket-less `TODO` in fixtures/cache_refresh.py as a `Stale
marker` finding.

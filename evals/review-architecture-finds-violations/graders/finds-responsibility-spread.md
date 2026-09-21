---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Responsibility spread` (or
  clearly equivalent category name) finding pointing out that the "Order
  total" concept from `.vibe/glossary.md` is implemented twice: once in
  `fixtures/core/pricing.py` (the canonical `calculate_total`) and again,
  independently, in `fixtures/utils/legacy_report.py`'s
  `export_weekly_csv`.
  FAIL if no finding names this concept implemented in both places.
weight: 1
---

Reports the "Order total" concept reimplemented in
`fixtures/utils/legacy_report.py` instead of reusing `core/pricing.py` as a
Responsibility spread finding.

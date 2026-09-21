---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Dead code` (or clearly equivalent
  category name) finding on `calculate_total_legacy` in
  fixtures/pricing.py, for a function nothing in fixtures/ calls anymore
  (superseded by `calculate_total`).
  FAIL if no finding flags `calculate_total_legacy` as dead code.
weight: 1
---

Reports `calculate_total_legacy` in fixtures/pricing.py as a `Dead code`
finding.

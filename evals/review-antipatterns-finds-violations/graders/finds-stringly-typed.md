---
type: llm
focus: last_message
criteria: |
  PASS if the reported findings include a `Stringly-typed code` (or clearly
  equivalent category name) finding on `apply_discount` in
  fixtures/pricing_rules.py, for branching on the bare string `tier`
  ("gold"/"silver"/"bronze") instead of an enum or constant.
  FAIL if no finding flags `apply_discount`'s string-based branching.
weight: 1
---

Reports `apply_discount`'s bare-string tier comparisons as a Stringly-typed
code finding.

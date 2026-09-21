---
type: tool_order
before:
  tool: Edit
  input_match: "stats\\.test\\.js"
after:
  tool: Edit
  input_match: "(?<!test)stats\\.js"
weight: 2
---

Deterministic red-before-green check: the test file must be edited before
the implementation file. Complements `tests-cover-required-cases` and
`tests-not-tautological` (which grade the reported narrative) with an
actual tool-call-order signal instead of relying on the model's own account.

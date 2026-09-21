---
type: tool_order
before:
  tool: Edit
  input_match: "list-utils\\.test\\.js"
after:
  tool: Edit
  input_match: "(?<!test)list-utils\\.js"
weight: 2
---

Deterministic red-before-green check: the reproducing test must be edited
into the test file before the source file is edited. Complements
`test-reproduces-bug-first` (which grades the reported narrative) with an
actual tool-call-order signal instead of relying on the model's own account.

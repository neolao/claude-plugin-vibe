---
type: tool_order
before:
  tool: Edit
  input_match: "pricing\\.test\\.js"
after:
  tool: Edit
  input_match: "src/money\\.js"
weight: 2
---

Deterministic red-before-green check: the reproducing test must be edited
into the test file before the source file is edited.

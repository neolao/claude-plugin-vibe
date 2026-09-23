---
type: tool_order
before:
  tool: Edit
  input_match: "src/roster\\.js"
after:
  tool: Bash
  input_match: "npm run build"
weight: 2
---

The Baseline check already runs the build command once before any code is
written. This grader checks the new behaviour specifically: the build
command is run again by Refactor and lint, strictly after the source file
was edited to add the new function — not only at baseline.

---
type: tool_used
tool: Bash
input_match: "npm run build"
min: 2
max: 999
weight: 2
---

The Baseline check already runs the build command once before any code is
written. This grader checks the new behaviour specifically: the build
command is run at least a second time, by Refactor and lint, after the
implementation — not only at baseline.

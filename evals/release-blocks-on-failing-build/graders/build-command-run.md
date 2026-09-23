---
type: tool_used
tool: Bash
input_match: "npm run build"
min: 1
max: 999
weight: 2
---

Step 2's pre-release checks must actually run the project's build command,
not just test and lint — checked as a real `npm run build` invocation, not
merely claimed in the report.

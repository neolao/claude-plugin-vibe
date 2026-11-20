---
type: tool_used
tool: Bash
input_match: "npm run (-s )?format|jsonfmt --write"
min: 1
max: 999
weight: 2
---

The violation is fixed by the project's own formatter, as Step 6 says,
not by a hand edit of the file.

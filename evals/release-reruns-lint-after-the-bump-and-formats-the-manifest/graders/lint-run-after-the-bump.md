---
type: tool_used
tool: Bash
input_match: "npm run (-s )?lint|jsonfmt --check|jsoncheck"
min: 2
max: 999
weight: 2
---

Lint runs twice at least: once in Step 2, once again after Step 5 bumped
`package.json`. A single run means the re-check never happened.

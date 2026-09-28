---
type: tool_used
tool: Bash
input_match: "test:e2e|--test e2e"
min: 1
max: 999
weight: 1
---

`npm test` only runs `test/`; the e2e tests sit behind the separate
`test:e2e` script in `fixtures/package.json`, which CLAUDE.md never
mentions. The agent's Step 1 says to run a separately excludable e2e suite
specifically — it must actually execute it, not just read it.

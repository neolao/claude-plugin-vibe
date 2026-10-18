---
name: claim-verifier-finds-unproven-and-contradicted
description: claim-verifier must flag "all 5 tests pass" as unproven (no command output, and the file holds 2 tests), "returns an empty list on an empty file" as contradicted by parser.py:9-10 (it raises), and "timeout of 30 seconds" as contradicted by parser.py:3 (60); the correct line-count claim is not a finding. Runs in Docker: Bash granted so the agent may re-run the cheap unit test.
tags: [claim-verifier, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Bash, Agent]
---

Invoke the `vibe:claim-verifier` sub-agent (Agent tool, `subagent_type: "vibe:claim-verifier"`) with exactly this prompt:

```
Check the claims of the text below. Use: report of a run. Working directory: the current directory; the code is in `fixtures/`.

TEXT TO CHECK:
"The contacts parser is done. `read_contacts` reads the file line by line and splits each line on commas (fixtures/parser.py:7-11). On an empty file it returns an empty list, so the caller never has to special-case it (fixtures/parser.py:9-10). The read timeout is set to 30 seconds (fixtures/parser.py:3). All 5 tests pass."

PROOFS PROVIDED BY THE CALLER: none beyond the line references in the text.
```

Once the sub-agent returns, report its output back verbatim.

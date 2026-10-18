---
name: requirements-reviewer-finds-gap-addition-and-breach
description: requirements-reviewer must report the uncovered sorting criterion as a gap, the unrequested JSON export as an addition, and the extra `fmt` parameter as a breach of the signature constraint — each citing the request and the code — and nothing else
tags: [requirements-reviewer, recall]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:requirements-reviewer` sub-agent (Agent tool, `subagent_type: "vibe:requirements-reviewer"`) with exactly this prompt:

```
Check the deliverable against the request. Type of use: code against its backlog item.

REQUEST: the file `fixtures/REQUEST.md` in the current directory.
DELIVERABLE: `fixtures/export.py` and `fixtures/test_export.py`.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.

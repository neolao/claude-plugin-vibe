---
name: requirements-reviewer-finds-a-refactor-the-request-did-not-need
description: >-
  requirements-reviewer must report the rewrite of `format_label`, a function the request never concerns, as an addition citing the diff hunk, while the total helper, the total line and the new test serve the request and are not findings
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
DELIVERABLE: the change since the baseline, as the diff `fixtures/change.diff`, and the files it leaves: `fixtures/export.py` and `fixtures/test_export.py`.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.

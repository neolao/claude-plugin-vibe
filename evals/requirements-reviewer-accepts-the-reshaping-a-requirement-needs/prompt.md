---
name: requirements-reviewer-accepts-the-reshaping-a-requirement-needs
description: >-
  requirements-reviewer must return exactly `none` when the change reshapes the function the total line lands in — a row-writing loop extracted into a helper so the total can follow it — and adds a total helper and a test, all of which serve the request
tags: [requirements-reviewer, precision]
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

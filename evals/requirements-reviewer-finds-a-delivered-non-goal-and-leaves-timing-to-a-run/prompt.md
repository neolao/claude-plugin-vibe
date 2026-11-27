---
name: requirements-reviewer-finds-a-delivered-non-goal-and-leaves-timing-to-a-run
description: >-
  requirements-reviewer must report the widened gallery thumbnails, which the request puts out of scope, as a breached constraint, and the 2-second budget, which only a run can establish, as an ambiguity naming the check — never as a breach
tags: [requirements-reviewer, recall, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:requirements-reviewer` sub-agent (Agent tool, `subagent_type: "vibe:requirements-reviewer"`) with exactly this prompt:

```
Check the deliverable against the request. Type of use: code against its brief.

REQUEST: the backlog item `fixtures/REQUEST.md` in the current directory.
DELIVERABLE (files changed since the baseline): `fixtures/uploads.py`, `fixtures/thumbnails.py` and `fixtures/test_uploads.py`.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.

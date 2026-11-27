---
name: requirements-reviewer-accepts-a-non-goal-left-alone
description: >-
  requirements-reviewer must return exactly `none` when the thumbnails the request puts out of scope are left untouched, every criterion is met by reading, and no dependency is added
tags: [requirements-reviewer, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:requirements-reviewer` sub-agent (Agent tool, `subagent_type: "vibe:requirements-reviewer"`) with exactly this prompt:

```
Check the deliverable against the request. Type of use: code against its brief.

REQUEST: the backlog item `fixtures/REQUEST.md` in the current directory.
DELIVERABLE (files changed since the baseline): `fixtures/uploads.py` and `fixtures/test_uploads.py`. The other files under `fixtures/` are the project's code, which this change did not touch.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.

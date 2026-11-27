---
name: requirements-reviewer-finds-the-gap-nothing-in-the-repository-covers
description: >-
  requirements-reviewer must report the refusal never recorded in the audit log as a gap, while the admin list criterion, met by an untouched file outside the changed files, is no gap
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
DELIVERABLE (files changed since the baseline): `fixtures/coupons.py` and `fixtures/test_coupons.py`. The other files under `fixtures/` are the project's code, which this change did not touch.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.


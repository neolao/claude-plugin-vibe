---
name: requirements-reviewer-no-false-positives
description: requirements-reviewer must return exactly `none` on a deliverable that meets every criterion — the start>end guard, the private helper and the tests serve the request and are not additions; string comparison of ISO dates respects the no-date-library constraint
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
DELIVERABLE: `fixtures/period.py` and `fixtures/test_period.py`.
No decision was taken after the request.
```

Once the sub-agent returns, report its output back verbatim.

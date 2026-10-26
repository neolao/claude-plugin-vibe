---
name: requirements-reviewer-honors-later-decision-and-finds-hidden-breach
description: >-
  requirements-reviewer must report the email missing the remaining quantity as a gap and the new dependency as a breached constraint, while treating the criterion dropped by a later decision and the criterion met in another file as no gap
tags: [requirements-reviewer, recall, precision]
runs: 3
max_turns: 10
timeout_seconds: 300
allowed_tools: [Read, Grep, Glob, Agent]
---

Invoke the `vibe:requirements-reviewer` sub-agent (Agent tool, `subagent_type: "vibe:requirements-reviewer"`) with exactly this prompt:

```
Check the deliverable against the request. Type of use: code against its backlog item.

REQUEST: the file `fixtures/REQUEST.md` in the current directory.
DELIVERABLE: `fixtures/notify.py`, `fixtures/hooks.py`, `fixtures/stock.py`, `fixtures/requirements.txt` and `fixtures/test_notify.py`.
Decision taken after the request: the product owner dropped criterion 3 (the dashboard notification); the email alone is enough.
```

Once the sub-agent returns, report its output back verbatim.

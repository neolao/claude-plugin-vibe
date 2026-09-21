---
name: backlog-splits-oversized-request
description: vibe:backlog must ask to split an oversized single-description request into separate items (naming the candidate titles), then create them as one batch with a single commit — requires --allow-tools Bash Write Edit to run
tags: [backlog, batch, scope-splitting]
runs: 3
max_turns: 20
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with this argument, verbatim:

```
add CSV export, add a dark mode, and add email notifications
```

This bundles three independently shippable capabilities into one request. Per the skill's own Step 6, this should trigger a question asking whether to split it into separate items before anything is created. If it asks, answer yes and let it proceed as a batch. Do not pre-emptively split the request yourself before invoking the skill — let the skill drive that decision.

Once it finishes, report back: the exact question it asked (if any), the files it created, and the commit it made.

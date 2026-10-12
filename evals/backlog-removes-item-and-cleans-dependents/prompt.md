---
name: backlog-removes-item-and-cleans-dependents
description: vibe:backlog remove must confirm first (warning that the item is in progress and naming the items that depend on it), then git rm the file, drop its number from each dependent's depends_on, and commit with the exact remove message — requires --allow-tools Bash Write Edit to run
tags: [backlog, remove, dependencies]
runs: 3
max_turns: 25
timeout_seconds: 450
allowed_tools: [Read, Glob, Grep, Skill, Bash, Write, Edit]
---

Invoke the `vibe:backlog` skill (Skill tool, `skill: "vibe:backlog"`) with this argument, verbatim:

```
remove 1
```

If the skill asks for confirmation, write the question out verbatim as a message of its own, before changing anything, then, without ending your turn (nobody else will reply), answer yes in a following message and let it proceed.

Once it finishes, report back: the exact confirmation question it asked (if any), the files it changed or removed, and the commit it made.

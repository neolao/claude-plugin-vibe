---
name: challenge-redirects-an-open-choice-to-consult
description: >-
  challenge must say that a choice still to make is not a decision, point to /vibe:consult and launch no advocate — never pick one side itself and attack it
tags: [challenge, recall]
runs: 3
max_turns: 12
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Invoke the `vibe:challenge` skill (Skill tool, `skill: "vibe:challenge"`) with this argument, verbatim:

```
Should the desktop app store its projects in SQLite or in one JSON file per project? We have not decided yet.
```

Nothing else was said about this choice in this conversation, and the workspace holds no project files.

If the skill asks you anything, do not answer it, and do not invent an answer on the user's behalf: end your turn right after its question. Otherwise report back exactly what it returned, in full.

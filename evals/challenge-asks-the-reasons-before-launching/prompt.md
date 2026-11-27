---
name: challenge-asks-the-reasons-before-launching
description: >-
  challenge must ask the user for the reasons behind a bare decision and the alternatives looked at, in one question, before launching the advocate — never fill them in itself and never attack a decision whose reasons it invented
tags: [challenge, recall]
runs: 3
max_turns: 12
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Invoke the `vibe:challenge` skill (Skill tool, `skill: "vibe:challenge"`) with this argument, verbatim:

```
we picked PostgreSQL over SQLite for the desktop app
```

Nothing else was said about this decision in this conversation, and the workspace holds no project files.

If the skill asks you anything, do not answer it, and do not invent an answer on the user's behalf: end your turn right after its question, which is then your final message, exactly as the skill wrote it. If it asks nothing, report back exactly what it returned, in full.

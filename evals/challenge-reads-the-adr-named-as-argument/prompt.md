---
name: challenge-reads-the-adr-named-as-argument
description: >-
  challenge given the path of a recorded ADR must read it as the account — decision, reasons, rejected alternatives — cite it by its path, ask nothing, and launch the advocate with those rejected alternatives in its prompt
tags: [challenge, recall]
runs: 3
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Invoke the `vibe:challenge` skill (Skill tool, `skill: "vibe:challenge"`) with this argument, verbatim:

```
.vibe/decisions/002-sqlite-local-store.md
```

The current workspace is the project that ADR belongs to: `.vibe/decisions/` holds the decision records and `app/` the code. Nothing else was said about this decision in this conversation.

If the skill asks you anything, do not answer it, and do not invent an answer on the user's behalf: end your turn right after its question. Otherwise report back exactly what it returned, in full.

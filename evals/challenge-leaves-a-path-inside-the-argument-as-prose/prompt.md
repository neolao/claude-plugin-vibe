---
name: challenge-leaves-a-path-inside-the-argument-as-prose
description: >-
  challenge given a decision written as prose that mentions a file path must take the prose as the decision — not read that path as the decision file, not switch to the ADR the repository holds — ask nothing, and launch the advocate with the prose's rejected alternatives
tags: [challenge, precision]
runs: 3
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent]
---

Invoke the `vibe:challenge` skill (Skill tool, `skill: "vibe:challenge"`) with this argument, verbatim:

```
We keep every runtime setting of the desktop app in config/app.toml rather than in environment variables. Reasons: one file to document, the support team edits it by hand, and the app is launched from a dock with no shell around it. Rejected: environment variables, because a dock launch gives the process none; a settings table in the SQLite store, because settings must be editable while the app is closed.
```

The current workspace is the project this decision belongs to: `app/` holds the code, `config/app.toml` the settings file, and `.vibe/decisions/` the decision records. Nothing else was said about this decision in this conversation.

If the skill asks you anything, do not answer it, and do not invent an answer on the user's behalf: end your turn right after its question. Otherwise report back exactly what it returned, in full.

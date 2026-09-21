---
name: feature-blocks-on-unmet-dependency-in-auto-mode
description: >-
  vibe:feature 002 --auto must stop at backlog resolution because 002 depends
  on 001, which is still todo — verdict AUTO-RESULT: blocked, item flipped to
  status: blocked with a ## Blocked section, changes committed, and no code
  written. The cheap counterpart to feature-implements-via-tdd-in-auto-mode:
  it exercises the --auto gate table's blocked path without paying for a TDD
  cycle. Requires `--allow-tools Bash,Write,Edit` to run.
tags: [feature, auto, blocked, backlog]
runs: 3
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:feature` skill (Skill tool, `skill: "vibe:feature"`) with exactly this argument:

```
002 --auto
```

Work in the current directory. It already contains a small Node.js project (a source module, its test file, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, a `.vibe/backlog/`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

Report the skill's final message verbatim, including that line.

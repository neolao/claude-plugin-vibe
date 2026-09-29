---
name: feature-blocks-on-duplicate-in-auto-mode
description: >-
  vibe:feature must stop at its duplicate check in --auto mode when the
  requested capability is already covered, under another wording, by an
  [Unreleased] CHANGELOG entry — verdict AUTO-RESULT: blocked — possible
  duplicate of ..., and no code, test or changelog written. Requires
  `--allow-tools Bash,Write,Edit` to run.
tags: [feature, auto, blocked, duplicate]
runs: 3
max_turns: 40
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:feature` skill (Skill tool, `skill: "vibe:feature"`) with exactly this argument:

```
add a function that returns the median of a list of numbers, raising a clear error for an empty list --auto
```

Work in the current directory. It already contains a small Node.js project (a source module, its test file, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

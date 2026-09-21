---
name: feature-implements-via-tdd-in-auto-mode
description: >-
  vibe:feature must run the full TDD cycle in --auto mode on a tiny,
  single-function brief and reach `AUTO-RESULT: done` end to end (expert
  consultation, red/green/runtime-verification/refactor loop, CHANGELOG,
  sync, commit) — the happy path, nothing in this fixture should legitimately
  block. Requires `--allow-tools Bash,Write,Edit` to run. This is the single
  most expensive case pattern in the whole eval suite: validate alone with
  `--runs 1` before folding it into a wider run.
tags: [feature, tdd, auto]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:feature` skill (Skill tool, `skill: "vibe:feature"`) with exactly this argument:

```
add a function that returns the sum of a list of numbers, raising a clear error on non-numeric input --auto
```

Work in the current directory. It already contains a small Node.js project (a source module, its test file, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

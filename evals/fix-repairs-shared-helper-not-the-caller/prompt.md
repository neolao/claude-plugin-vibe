---
name: fix-repairs-shared-helper-not-the-caller
description: >-
  vibe:fix must trace a symptom reported on `orderTotal` back to its root
  cause in the shared `roundCents` helper (a different file) and fix it
  there, not patch the reported caller, in --auto mode, and reach
  `AUTO-RESULT: done`. Requires `--allow-tools Bash,Write,Edit` to run.
tags: [fix, tdd, auto, root-cause]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:fix` skill (Skill tool, `skill: "vibe:fix"`) with exactly this argument:

```
orderTotal([{ price: 1.005, qty: 1 }]) returns 1 but it should return 1.01 --auto
```

Work in the current directory. It already contains a small Node.js project (a pricing module built on a currency helper module, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

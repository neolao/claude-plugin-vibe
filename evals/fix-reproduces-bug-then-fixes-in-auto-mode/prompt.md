---
name: fix-reproduces-bug-then-fixes-in-auto-mode
description: >-
  vibe:fix must reproduce a real, deliberately planted bug with a failing
  test first (red), then fix the root cause (green), in --auto mode, and
  reach `AUTO-RESULT: done`. Requires `--allow-tools Bash,Write,Edit` to run.
  Like the sibling `feature` case, this exercises the skill's full workflow
  (baseline check, red/green/runtime-verification/refactor loop, CHANGELOG,
  sync, commit) and is expensive: validate alone with `--runs 1` first.
tags: [fix, tdd, auto]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:fix` skill (Skill tool, `skill: "vibe:fix"`) with exactly this argument:

```
max([-5, -2, -9]) returns 0 but it should return -2, the largest number in the list --auto
```

Work in the current directory. It already contains a small Node.js project (a source module with the bug described above, its test file — which does not currently cover this path — a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

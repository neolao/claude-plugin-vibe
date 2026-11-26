---
name: fix-corrects-a-test-that-pinned-the-bug
description: >-
  vibe:fix on a bug that an existing test asserts as the expected output
  (`formatDuration(125)` pinned to "2:5"). The fix must change the code and
  correct that wrong assertion, not keep it green with a special case, in
  --auto mode, and reach `AUTO-RESULT: done`. Requires
  `--allow-tools Bash Write Edit` to run.
tags: [fix, tdd, auto, wrong-test]
runs: 1
max_turns: 140
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit, TaskCreate, TaskUpdate]
---

Invoke the `vibe:fix` skill (Skill tool, `skill: "vibe:fix"`) with exactly this argument:

```
formatDuration(65) returns "1:5" but the timer should read "1:05" --auto
```

Work in the current directory. It already contains a small Node.js project (a time-formatting module, its test file, a passing `npm test` / `npm run lint` baseline, a `CHANGELOG.md`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.

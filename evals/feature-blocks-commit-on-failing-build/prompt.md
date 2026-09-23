---
name: feature-blocks-commit-on-failing-build
description: >-
  vibe:feature must re-run the project's build command during Refactor and
  lint, and must not reach Commit while it fails, in --auto mode, reaching
  `AUTO-RESULT: done` only once the build is actually green. Requires
  --allow-tools Bash,Write,Edit to run. Expensive (full --auto TDD loop):
  validate alone with --runs 1 first.
tags: [feature, tdd, auto, build-gate]
runs: 1
max_turns: 80
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Agent, Bash, Write, Edit]
---

Invoke the `vibe:feature` skill (Skill tool, `skill: "vibe:feature"`) with exactly this argument:

```
add a function that returns a roster's average score, reusing the existing total, and raises a clear error for an empty roster --auto
```

Work in the current directory. It already contains a small Node.js project (source modules, a test file, a passing `npm test` / `npm run lint` / `npm run build` baseline, a `CHANGELOG.md`, and a git repository with one commit) — do not recreate any of this. Follow the skill's own instructions exactly, including its `--auto` mode gate table from `workflow.md`. There is no one to answer a question: every gate must resolve itself and the run must end with a machine-readable `AUTO-RESULT:` line.
